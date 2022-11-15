import requests
from datetime import datetime as dt
r = requests.get('https://a.4cdn.org/pol/catalog.json')
r = r.json()
def gen_chan():
    for idx, page in enumerate(r):
        for thread in r[idx]['threads']:
            yield thread
def get_threads(key: str, default='NaN'):
    return threads.get(key, default)

i = 0
for threads in gen_chan():
    i += 1
    print(i)
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
