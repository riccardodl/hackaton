import typing
import os
import json
import tempfile
import urllib.request

from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


def _download_file(download_url):
    base_name = os.path.basename(download_url)
    response = urllib.request.urlopen(download_url)    
    file_name = os.path.join(_get_tmp_folder(), base_name + ("" if base_name.endswith('.pdf') else ".pdf"))
    try:
        with open(file_name, 'wb') as f:
            f.write(response.read())
        return file_name
    except:
        return None

def _get_tmp_folder():
    return tempfile.gettempdir()


def _get_raw_text_from_pdf(path_pdf):
        
    try:
        extractor = SimpleTextExtraction()
        d: typing.Optional[Document] = None
        with open(path_pdf, "rb") as pdf_in_handle:
            d = PDF.loads(pdf_in_handle, [extractor])
            if d:
                pages = d.get('XRef', {}).get('Trailer', {}).get('Root', {}).get('Pages', {}).get('Count', 0) # There is not method to know how many pages are there.
                text = []
                for page in range(int(pages)):
                    page_text = extractor.get_text_for_page(page)
                    print(page_text)
                    print('0---------------------\n\n----------------------')
                    text.append(page_text)

                return "\n".join(text)
    except Exception:
        print('------>>>>>> ERROR >>>>>>-------')

    return None

def _get_json_text_from_pdf(path_pdf):
    # Parse the pdf
    
    try:
        d: typing.Optional[Document] = None
        with open(path_pdf, "rb") as pdf_in_handle:
            d = PDF.loads(pdf_in_handle)
            if d:
                return json.dumps(d.to_json_serializable())

    except Exception:
        print('------>>>>>> ERROR >>>>>>-------')
    
    return None

def _print_json_pretty(json_str):
    j = json.load(json_str)
    print(json.dumps(j, indent=4, sort_keys=True))


def parse_pdf_prospect(url_pdf, json_format = True):
    '''
    Parses a pdf given as a filename to a json string
    :param filename: str representing a valid path
    :return: str # The json representation. Raises if no valid filename or operations fails
    '''

    # Try to download the pdf
    tmp_copy = _download_file(url_pdf)
    if not tmp_copy:
        raise RuntimeError

    if not os.path.exists(tmp_copy) or os.path.isdir(tmp_copy):
        raise IOError

    if json_format:
        return _get_json_text_from_pdf(tmp_copy)
    return _get_raw_text_from_pdf(tmp_copy)

def _tests():
    example_files = [
        'https://www.aspirin.de/sites/g/files/vrxlpx15691/files/2021-03/aspirin-500mg-ueberzogene-tabletten-beipackzettel.pdf'
    ]
    for f in example_files:
        d = parse_pdf_prospect(f, False)
        if d:
            print(d)
        d = parse_pdf_prospect(f, True)
        if d:
            with open('/Users/raulcatena/Desktop/ej.json', 'w') as wr:
                wr.write(d)


if __name__ == "__main__":
    _tests()