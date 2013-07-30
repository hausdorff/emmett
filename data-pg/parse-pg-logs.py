from __future__ import with_statement
import json, urlparse


QS_SCRIPTS = ['web_exec_py2.py','web_exec_py3.py', 'web_exec_py2-1.py',
              'web_exec_py3-1.py']

def records ():
    with open('all.txt') as f:
        return f.readlines()

def qs_to_dict ():
    d = {}
    for i,r in enumerate(records()):
        p = urlparse.parse_qs(r)
        if 'user_script' in p:
            #print p['user_script'][0]
            d[i] = p['user_script'][0]
    return d

def wo_data (fn, d):
    with open(fn, 'w') as w:
        w.write(json.dumps(qs_to_dict()))


if __name__ == '__main__':
    wo_data('all_progs.txt', qs_to_dict())
