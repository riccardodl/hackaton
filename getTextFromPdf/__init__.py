import logging
#from ..shared_code import database
import azure.functions as func
import csv
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    barcode = req.params.get('barcode')
    
    if not barcode:
        return func.HttpResponse("Missing param",status_code=400)

    logging.info(f"{barcode}")
    db_handler = Database()
    data = db_handler.get_entry(barcode)
    
    if data:
        return func.HttpResponse(f"{data}")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a barcode.",
            status_code=200
        )

class Database(object):
    def __init__(self):        
        self.filepath = 'database.csv'

    def get_next_id(self):
        if not os.path.exists(self.filepath):
            return 0
            
        with open(self.filepath, newline='') as file:
            data = csv.reader(file)
            count = len(list(data))
            return count


    def get_entry(self, drug_name):
        with open(self.filepath, newline='') as file:
            data = csv.reader(file)
            for row in data:
                if row[1] == drug_name:
                    return row[3]
    
            return 'Entry not found'

    def put_entry(self, barcode_id, drug_name, barcode_type, json):    
        if os.path.exists(self.filepath):
            os.unlink(self.filepath)    
        with open(self.filepath, 'a+', newline='') as file:
            writer = csv.writer(file)            
            writer.writerow([barcode_id,drug_name,barcode_type,json])
        return None


