# -*- coding: utf-8 -*-
import json
tweets = list(open('tweets.json','rt'))
with open("Filtered_urls.txt", "w", encoding='utf-8')as f:
    for t in tweets:
        t = json.loads(t)
        try:
            if len(t['entities']['urls']) != 0: #urls
                for h in t['entities']['urls']:
                    f.write(h['url']+'\n')  #url
        except KeyError:
            pass