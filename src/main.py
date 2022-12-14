import json
import requests
from pprint import pprint
from datetime import datetime as dt
import time
import pandas
import os

boards = [
    '3','a','aco','adv','an','b','bant',
    'biz','c','cgl','ck','cm','co','d',
    'diy','e','f','fa','fit','g','gd',
    'gif','h','hc','his','hm','hr','i',
    'ic','int','jp','k','lgbt','lit','m',
    'mlp','mu','n','news','o','out','p',
    'po','pol','pw','qa','qst','r','r9k',
    's','s4s','sci','soc','sp','t','tg',
    'toy','trash','trv','tv','u','v','vg',
    'vip','vm','vmg','vp','vr','vrpg',
    'vst','vt','w','wg','wsg','wsr','x',
    'xs','y']

timestr = time.strftime("%Y%m%d-%H") 

for board in boards:

    r = requests.get('https://a.4cdn.org/' + board + '/catalog.json')
    r = json.loads(r.text)

    threads = []
    for page in r: 
        for thread in page['threads']:
            t = requests.get(f'https://a.4cdn.org/{board}/thread/{thread["no"]}.json')
            t = json.loads(t.text)
            threads.append(t)

    folder = 'data/' + board + '/'

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = board + 'Data' + timestr
    filename_json = folder + filename + '.json'

    with open(filename_json, 'w') as json_file:
        json.dump(threads, json_file) # write to json file
    
    print(board)

end = time.time()
print(end - start)