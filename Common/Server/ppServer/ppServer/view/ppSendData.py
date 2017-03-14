# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse



def send_data_to_project(pro_name, description, item_name):
    url = 'http://119.29.40.39/api/v1/initdata/projects/set_project_info/'
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent' : user_agent}
    sendData = {
        'pro_name': pro_name,
        'description': r''+description,
        'item_name': ''+item_name
    }
    data = urllib.parse.urlencode(sendData).encode(encoding='UTF8')
    req = urllib.request.Request(url, data, headers)
    res = urllib.request.urlopen(req)
    result = res.read()
    print(result)



def send_data_to_proitem(pro_name, item_key, values):
    url = 'http://119.29.40.39/api/v1/initdata/items/set_proitem_value/'
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    sendData = {
        'pro_name': pro_name,
        'item_key': item_key,
        'values': values
    }
    data = urllib.parse.urlencode(sendData).encode(encoding='UTF8')
    req = urllib.request.Request(url, data, headers)
    res = urllib.request.urlopen(req)
    result = res.read()
    print(result)


if __name__ == '__main__':
    for i in range(200000):
        send_data_to_project('11' + str(i), '文档代码一体化', '~~~')
        # send_data_to_proitem('Comb_Analyze', 'Inspector_Object', '123' + str(i))