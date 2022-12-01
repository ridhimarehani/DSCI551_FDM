import json
import sys

def conver_dynamo_to_json(json_content, dynamo_dt):
    json_content_type = type(json_content)
    #if the content is of list type, convert the individual contents of list as per their type
    if json_content_type is list:
        temp_list = []
        for index in json_content:
            temp_list.append(conver_dynamo_to_json(index,dynamo_dt))
        json_content = temp_list
        return json_content

    #if content is of type map 
    elif json_content_type is dict:
        for key in json_content.keys():
            # check if the map's key matches the defined datatypes
            if key in dynamo_dt:
                if key == 'S':
                    json_content = str(json_content[key])
                elif key == 'N':
                    temp_str = json_content[key]
                    if '.' in temp_str:
                        json_content = float(temp_str)
                    else:
                        json_content = int(temp_str)
                elif key == 'NS':
                    tempSet = []
                    for val in json_content[key]:
                        if '.' in val:
                            tempSet.append(float(val))
                        else:
                            tempSet.append(int(val))
                    json_content = tempSet
                elif key == 'L' or key == 'M' or key == 'SS':
                    json_content = conver_dynamo_to_json(json_content[key],dynamo_dt)
                break
            # if map's key doesnt match the defined data types, recursion for the next level
            else:
                json_content[key] = conver_dynamo_to_json(json_content[key],dynamo_dt)
        return json_content

    # if the content is niether map nor list, we have reached the root element
    else:
        return json_content

def main():
    DYNAMO_DATATYPE = ("S", "N", "L", "M", "SS", "NS")
    
    args = sys.argv
    input_file = args[1]
    output_file = args[2]

    book_dict = {}

    with open(input_file, 'r') as j:
     book_dict = json.loads(j.read())
    output = open(output_file, 'w')
    dynamo_to_json = conver_dynamo_to_json(book_dict, DYNAMO_DATATYPE)
    output.write(json.dumps(dynamo_to_json, indent=4))
    output.close()

if __name__ == "__main__":
    main()