from client import Client
import time

# from vk import Vk
class Vk: 
    '''
    Выполняет авторизацию, возвращает некоторую информацию о профиле...
    ''' 
    def __init__(self, token):
        self.client = Client()
        self.token = token
        self.v = "5.120"
    
    def check_auth(self):
        result = self.client.get('https://api.vk.com/method/users.get?&access_token=' + self.token + f'&v={self.v}').json()
        return not result.get('response') is None
    
    def get_wall(self, id, offset, filters = 'others'): #https://vk.com/dev/wall.get
        result = self.client.get(f'https://api.vk.com/method/wall.get?filter={filters}&owner_id={id}&count=100&offset={offset}&access_token={self.token}&v={self.v}').json()
        return result.get("response")