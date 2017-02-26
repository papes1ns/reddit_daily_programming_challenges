# https://www.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/

import random
from datetime import datetime
s = datetime.now()

patron_stream = open('secret_santa_patrons', 'r')

patron_list = []
for line in patron_stream.readlines():
    parsed_list = line.split()
    for patron in parsed_list:
        patron_list.append({
            'name': patron,
            'relations': [p for p in parsed_list if p != patron],
            'recieved': False})

assignment = {}
for patron in patron_list:
    a = patron
    not_recieved = [d for d in patron_list if d['recieved'] == False]

    b = None
    while b is None:
        b = random.choice(not_recieved)
        if b['name'] not in a['relations'] and a['name'] != b['name']:
            assignment[a['name']] = b['name']
            b['recieved'] = True
        else:
            b = None

# for k, v in assignment.items():
#     print "%s => %s" % (k, v)

print "Runtime: %s" % (datetime.now() - s)
