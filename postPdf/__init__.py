import logging
from shared.database import Database
from shared.pdf_parser import *
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    drug = req.params.get('drug')
    qr_code = req.params.get('qr_code')
    url = req.params.get('pdf_url')
    if not qr_code or not url or not drug:
        return func.HttpResponse("Missing param",status_code=400)



    data = parse_pdf_prospect(url, False)  
    data = data.replace('\r','').replace('\n','<br />') 


    db_handler = Database()
    id = db_handler.get_next_id()
    db_handler.put_entry(id, drug, qr_code, data)

    return func.HttpResponse("OK",status_code=200)
