from operator import le
from wsgiref.util import request_uri
import requests
import sys
import json
#TBD: check inclusive in range, check output format
def main():
    args = sys.argv
    start_range = args[1]
    end_range = args[2]
    # start_range = 10000
    # end_range = 10500
    request_url = 'https://dsci551-a858f-default-rtdb.firebaseio.com/question1.json?orderBy="price"&startAt=' + str(start_range) + '&endAt='+str(end_range)
    x = requests.get(request_url)
    res = json.loads(x.text)
    res_list = []
    if len(res) == 0:
        print('No cars found with the given range')
    else:
        # print('-------------')
        for key in res:
            res_list.append(res[key]['car_ID'])
    print('IDs for the car price range are:')
    print(res_list, len(res_list))
    # &price={"gt":10298}
    # &limitToFirst=5

if __name__ == "__main__":
    main()
