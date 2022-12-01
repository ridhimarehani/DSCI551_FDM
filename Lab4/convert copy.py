import json
import os
import sys

DYNAMO_DATATYPE = {
    "S": lambda x: str(x),
    "B": lambda x: bool(x),
    "N": lambda x: str(x),
    "L": lambda x: conver_dynamo_to_json(x),
    "M": lambda x: conver_dynamo_to_json(x),
    "SS": lambda x: conver_dynamo_to_json(x),
    "NS": lambda x: conver_dynamo_to_json(x),
}

def conver_dynamo_to_json(raw):
    print('operation on-> ',raw)
    raw_type = type(raw)

    if raw_type is list:
        raw_list = []
        for index in raw:
            raw_list.append(conver_dynamo_to_json(index))
        raw = raw_list
        return raw

    elif raw_type is dict:
        for key in raw.keys():
            print('key> ',key)
            if key in DYNAMO_DATATYPE.keys():
                raw = DYNAMO_DATATYPE[key](raw[key])
                print('try raw> ',raw)
                break
            else:
                raw[key] = conver_dynamo_to_json(raw[key])
            # try:
            #     raw = DYNAMO_DATATYPE[key](raw[key])
            #     print('try raw> ',raw)
            #     break
            # except:
            #     raw[key] = conver_dynamo_to_json(raw[key])
            #     print('catch raw> ',raw)
            print('---------------------')
        return raw

    else:
        return raw

def main():

    # args = sys.argv
    # input_file = args[1]
    # output_file = args[2]

    input_file = 'HW3/input.json'
    output_file = 'HW3/output.json'

    book_dict = {}
    with open(input_file, 'r') as j:
     book_dict = json.loads(j.read())
    
    # output_file_path = "{}/{}".format(os.getcwd(), output_file)
    output = open(output_file, 'w')
    dynamo_to_json = conver_dynamo_to_json(book_dict)
    output.write(json.dumps(dynamo_to_json, indent=4))
    output.close()



if __name__ == "__main__":
    main()