import csv
import os


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


