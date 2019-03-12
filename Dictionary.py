import requests

class Dictionary:
    def __init__(self,api,app_id="",app_key=""):
        self.api = api
        self.headers = {'app_id':app_id, 'app_key':app_key}
        
    def is_word(self,word):
        try:
            if self.headers['app_id']=="" and self.headers['app_key']=="":
                response = requests.get("{0}{1}".format(self.api,word))#,headers=self.headers if self.headers['app_id']!="" else None)
            else:
                response = requests.get("{0}{1}".format(self.api,word),headers=self.headers)
            if response.status_code == 200:
                return True
            return False
        except Exception as e:
            print("Error :",e)


