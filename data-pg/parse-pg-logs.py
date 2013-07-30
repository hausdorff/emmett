from __future__ import with_statement
import json, urlparse


QS_SCRIPTS = ['web_exec_py2.py','web_exec_py3.py', 'web_exec_py2-1.py',
              'web_exec_py3-1.py']

def records ():
    """Gets each line in the file of preproc'd query strings; each line is one
    query string."""
    with open('all.txt') as f:
        return f.readlines()

def qs_to_dict ():
    """Turn a list of query strings into a dictionary of python programs. Each
    key is ordering in which we encountered the query string, ie, the value
    associated with the number 3 is the fourth query string we encountered.

    NOTE: we're not using `enumerate` because some query strings are empy, and
    that would result in some some numbers not being entered in the table."""
    d = {}
    i = 0
    for r in records():
        p = urlparse.parse_qs(r)
        if 'user_script' in p:
            #print p['user_script'][0]
            d[i] = p['user_script'][0]
            i += 1
    return d

def wo_dict_as_json (fn, d):
    """Write-out dictionary data as JSON"""
    with open(fn, 'w') as w:
        w.write(json.dumps(qs_to_dict()))


if __name__ == '__main__':
    wo_dict_as_json('all_progs.txt', qs_to_dict())
