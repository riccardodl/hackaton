from flask import Flask
from flask import request
from .database import Database

app = Flask(__name__)

#TODO get string and a qr code type, pull pdf form db, import module from raul that processes the pdf and return a json string

@app.route("/get/barcode/<barcode>", methods=['GET'])
def get_json(barcode):
    db_handler = Database()
    data = db_handler.get_entry(barcode)
    return data

#HTML forms must use enctype=multipart/form-data or files will not be uploaded.
@app.route("/put/<drug>", methods=['PUT'])
def put_json(drug):
    qr_code = request.form['qr_code']
    #pdf = request.files['pdf'] uncomment once we send a pdf file in the request

    db_handler = Database()
    id = db_handler.get_next_id()
    db_handler.put_entry(id, drug, qr_code, 'pdf')
    return 'Success'




