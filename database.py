import json
import csv

class Database(object):
    def __init__(self):
        super().__init__()

    def get_next_id(self):
        with open('database.csv', newline='') as file:
            data = csv.reader(file)
            count = len(list(data))
            return count


    def get_entry(self, drug_name):
        with open('database.csv', newline='') as file:
            data = csv.reader(file)
            for row in data:
                if row[1] == drug_name:
                    return row[3]
    
            return 'Entry not found'

    def put_entry(self, barcode_id, drug_name, barcode_type, pdf):
        json = Database.pdf_to_json(pdf)
        with open('database.csv', 'a+', newline='') as file:
            writer = csv.writer(file)            
            writer.writerow([barcode_id,drug_name,barcode_type,json])
        return None

    @classmethod
    def pdf_to_json(self, pdf):        
        data = pdf.decode('utf8')
        # Convert
        return f'{data}_but_in_json'
        
