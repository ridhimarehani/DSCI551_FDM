import sys
import pandas as pd
import requests
import json
import csv


def main():
    args = sys.argv
    cars_csv = args[1]
    print('yes',cars_csv)
    
    # df = pd.read_csv(cars_csv)
    # tmp = df.to_dict()
    # df.to_json (r'new_cars.json')
    # jsondata = json.dumps("new_cars.json")
    # jd = {"te" : "test"}
    json_data = {}
    # i = 0
    # j = 0
    with open(cars_csv, 'r') as fobj:
        csv_reader = csv.DictReader(fobj)
        for row in csv_reader:
            # Use one of the CSV column names as a key
            for key in row:
                if key == "price" or key == "compressionratio" or key == "carheight" or key == "carwidth" or key == "carlength" or key == "wheelbase" or key == "boreratio" or key == "stroke" or key == "horsepower" or key == "peakrpm" or key == "citympg" or key == "highwaympg" or key == "curbweight":
                    row[key] = float(row[key])
                
                if key == 'car_ID':
                    row[key] = int(row[key])

                # if j < 100:
                #     print('key> ',key)
                #     j+=1
            key1 = row['car_ID']
            # if(i<5):
            #     print(row)
            #     i+=1
            json_data[key1] = row 
    
    result = requests.put(url="https://dsci551-a858f-default-rtdb.firebaseio.com/question1.json", json= json_data)
    print(result)

if __name__ == "__main__":
    main()