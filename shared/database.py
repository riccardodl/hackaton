import json
import csv
import os

filepath = 'shared/database.csv'

class Database(object):
    def __init__(self):
        super().__init__()

    def get_next_id(self):
        with open(filepath, newline='') as file:
            data = csv.reader(file)
            count = len(list(data))
            return count


    def get_entry(self, drug_name):
        with open(filepath, newline='') as file:
            data = csv.reader(file)
            for row in data:
                if row[1] == drug_name:
                    return row[3]
    
            return 'Entry not found'

    def put_entry(self, barcode_id, drug_name, barcode_type, json):    
        os.unlink(filepath)    
        with open(filepath, 'a+', newline='') as file:
            writer = csv.writer(file)            
            writer.writerow([barcode_id,drug_name,barcode_type,json])
        return None


