import sys
import csv
from tokenize import tokenize
import string
import re
import requests
from collections import defaultdict
import json

def main():
    args = sys.argv
    cars_csv = args[1]
    json_data = defaultdict(list)
    
    
    with open(cars_csv, 'r') as fobj:
        csv_reader = csv.DictReader(fobj)
        for row in csv_reader:
            tokenized_key1 = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", row["CarName"])
            tokenized_key = tokenized_key1.strip().lower()
            json_data[tokenized_key].append(int(row["car_ID"]))
            key_list = tokenized_key.split(" ")
            if len(key_list) > 1:
                for tok in key_list:
                    if len(tok) > 0:
                        json_data[tok].append(int(row["car_ID"]))

    print('json_data> ',json_data)
    result = requests.put(url="https://dsci551-a858f-default-rtdb.firebaseio.com/question2.json", json=json_data)
    print(result)
            

if __name__ == "__main__":
    main()