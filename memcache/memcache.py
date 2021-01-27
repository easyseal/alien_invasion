import pymemcache
import time
import json

def get_data():
    data = {'iphone' : ['iphone6','iphone7'],'Android' : ['oppo','vivo']}
    time.sleep(5)
    return data

def show_data(data):
    for k,v in data.items():
        print(f"{k} : {v}")

def set_memcache(k,data):
    try:
        client = pymemcache.client.base.Client(('192.168.43.145','11211'))
        client.set(k,json.dumps(data))
        return True
    except Exception as e:
        print(e)
        return False

def get_memcache(k):
    try:
        client = pymemcache.client.base.Client(('192.168.43.145','11211'))
        return json.loads(client.get(k))
    except Exception as e:
        print(e)
        return False

def man():
    k = "Phone_menu"
    result = get_memcache(k)
    if result:
        print("this data get from memcache")
        show_data(result)
    else:
        print("this data get from mysql")
        data = get_data()
        show_data(data)
        set_memcache(k,data)

man()
