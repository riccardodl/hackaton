from flask import Flask
from flask import request
import json
import csv

app = Flask(__name__)


@app.route("/get/barcode/<barcode>", methods=['GET'])
def get_json(barcode):
    db_handler = Database()
    data = db_handler.get_entry(barcode)
    return data

#HTML forms must use enctype=multipart/form-data or files will not be uploaded.
@app.route("/put/<drug>", methods=['PUT'])
def put_json(drug):
    qr_code = request.form['qr_code']
    #pdf = request.files['pdf']

    db_handler = Database()
    id = db_handler.get_next_id()
    db_handler.put_entry(id, drug, qr_code, 'pdf')
    return 'Success'


#TODO get string and a qr code type, pull pdf form db, import module from raul that processes the pdf and return a json string


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
                elem = row[0].split(',', 4)
                if elem[1] == drug_name:
                    return elem[3]
                else:
                    break         
    
            return 'Entry not found'

    def put_entry(self, barcode_id, drug_name, barcode_type, pdf):
        json = Database.pdf_to_json(pdf)
        with open('database.csv', 'w+', newline='') as file:
            writer = csv.writer(file)
            row = f'{barcode_id},{drug_name},{barcode_type},{json}'
            writer.writerow([row])
        return None

    @classmethod
    def pdf_to_json(self, pdf):
        return 'json'


