import json
import requests
from pprint import pprint
from datetime import datetime as dt
import time

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

boardTest = ['pol']

# for board in boards:
for board in boardTest:

    r = requests.get('https://a.4cdn.org/' + board + '/catalog.json')
    r = r.json()

    r = requests.get('https://a.4cdn.org/' + board + '/catalog.json')
    r = json.loads(r.text)
    timestr = time.strftime("%Y%m%d-%H")
    # filename = '../data/' + board + '/data' + timestr + '.json'
    filename = './data/data' + timestr + '.json'

    with open(filename, 'w') as json_file:
        json.dump(r, json_file) #code for writing to a json_file


    # print(r[0]["threads"])  # nested info

    # print(r[0]["threads"][0]["com"])  # specific text on one thread

    # pprint(r)

    #words to use - trump

    #4CHAN CODE 

    def gen_chan():
        for idx, page in enumerate(r):
            for thread in r[idx]['threads']:
                yield thread


    def get_threads(key: str, default='NaN'):
        return threads.get(key, default)


    for threads in gen_chan():
        no = get_threads('no')
        now = get_threads('now')
        time = get_threads('time')
        my_time = dt.today()
        # com = TextMaster.strip_html(get_threads('com'))
        name = get_threads('name')
        trip = get_threads('trip')
        ids = get_threads('id')
        capcode = get_threads('capcode')
        filename = get_threads('filename') + get_threads('ext')
        resto = get_threads('resto')
        semantic_url = get_threads('semantic_url')
        replies = get_threads('replies')
        images = get_threads('images')
        # url = TextMaster.extract_url(get_threads('com'))
        # sent = TextMaster.textblob_sentiment(get_threads('com'))
        if 'last_replies' in threads:
            for comment in threads['last_replies']:
                com_com = comment.get('com', 'NaN')
                resto_com = comment.get('resto', 'NaN')
                now_com = comment.get('now', 'NaN')
                time_com = comment.get('time', 'NaN')
                fname_com = comment.get('filename', 'NaN')
                url_com = comment.get('com')
                sent_com = comment.get('com')
