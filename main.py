from flask import Flask
import json
import csv

app = Flask(__name__)


@app.route("/get/barcode/<barcode>")
def get_json(barcode):
    db_handler = Database()
    data = db_handler.get_entry(barcode)
    return data

@app.route("/put/json")
def put_json(barcode):
    db_handler = Database()
    data = db_handler.put_entry('id','paroxitin','qr_code','nice_pdf')
    return None


#TODO get string and a qr code type, pull pdf form db, import module from raul that processes the pdf and return a json string


class Database(object):
    def __init__(self):
        super().__init__()
        


    def get_entry(self, barcode_id):
        with open('database.csv', newline='') as file:
            data = csv.reader(file)
            for row in data:
                #elem = row.split(',', 4)
                if row[0] == barcode_id:
                    return row[3]
                else:
                    break         
    
            return 'Entry not found'

    def put_entry(self, barcode_id, drug_name, barcode_type, pdf):
        json = Database.pdf_to_json(pdf)
        with open('database.csv', newline='') as file:
            writer = csv.writer(file, delimiter='\n', quotechar='|')
            writer.writerow(barcode_id, drug_name, barcode_type, json)
        pass

    @classmethod
    def pdf_to_json(self, pdf):
        return 'json'


