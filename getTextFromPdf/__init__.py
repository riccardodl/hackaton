import logging
from shared.database import Database
from shared.pdf_parser import *
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    barcode = req.params.get('barcode')
    
    if not barcode:
        return func.HttpResponse("Missing param",status_code=400)

    db_handler = Database()
    data = db_handler.get_entry(barcode)
    if data:
        return func.HttpResponse(f"{data}")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a barcode.",
            status_code=200
        )
