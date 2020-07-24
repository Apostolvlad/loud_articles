import requests
# from client import Client
class Client:
    def __init__(self, user_agent = None): # 
        self.session = requests.Session() 
        if user_agent != None: self.session.headers.update({'User-Agent': user_agent})

    def get(self, url, params = ()): return self.session.get(url, params = params, timeout=60, verify = True)