'''
http://docs.python-requests.org/en/master/user/quickstart/
'''

import requests

res = requests.get("http://www.google.com")

print res.text