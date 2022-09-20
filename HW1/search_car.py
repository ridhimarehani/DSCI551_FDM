from collections import defaultdict
import json
from operator import le
from pickle import FALSE, TRUE
import sys
import re
import requests
import numpy as np

def main():
    args = sys.argv
    search_keyword = args[1]
    tokenized_key1 = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", search_keyword)
    fin_result = []
    print('tokenized_key1>',tokenized_key1)

    request_url = 'https://dsci551-a858f-default-rtdb.firebaseio.com/question2.json?orderBy="$key"&equalTo="'+tokenized_key1+'"'
    print(request_url)
    x = requests.get(request_url)
    print(x.text)
    res = json.loads(x.text)
    if res and tokenized_key1 in res:
        fin_result = res[tokenized_key1]
    print('fin_result1>>>>',fin_result)
    print('res>',res)
    print(len(res))
    
    # fin_result2 = []
    token_keywords = tokenized_key1.split(' ')
    print(token_keywords)
    if len(token_keywords) > 1:
        for token_key in token_keywords:
            req_url = 'https://dsci551-a858f-default-rtdb.firebaseio.com/question2.json?orderBy="$key"&equalTo="'+token_key+'"'
            print(req_url)
            x1 = requests.get(req_url)
            res1 = json.loads(x1.text)
            print("res1>", res1)
            
            if res1 and token_key in res1:
                for car_id in res1[token_key]:
                    if car_id not in fin_result:
                        fin_result.append(car_id)

    print(fin_result)
    if len(fin_result) == 0:
        print('No cars found')
    else:
        print('IDs of the car are:')
        print(fin_result)


def token_counter():
    args = sys.argv
    search_keyword = args[1]
    tokenized_key1 = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", search_keyword)
    input_car_name = tokenized_key1.strip()
    result = defaultdict(list)
    tokens = input_car_name.split(" ")
    counter = defaultdict(int)

    for token in tokens:
        req_url = 'https://dsci551-a858f-default-rtdb.firebaseio.com/question2.json?orderBy="$key"&equalTo="'+token+'"'
        req_result = requests.get(req_url)
        req_result = json.loads(req_result.text)

        if req_result and token in req_result:
            result[token] = req_result[token]
            for id in req_result[token]:
                counter[id] += 1

    # print(result)
    # print(counter)
    # print(sorted(counter.items(), key=lambda kv: (kv[1], kv[0])))
    result_list = sorted(counter.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    # print(result_list)
    # result1 = result1.reverse()
    # print(result1)
    id_list = []
    for key, _ in result_list:
        id_list.append(key)
    if len(id_list) == 0:
        print('No cars found')
    else:
        print('IDs of the car are:')
        print(id_list)

if __name__ == "__main__":
    # main()
    token_counter()