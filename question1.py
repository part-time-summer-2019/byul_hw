import requests
import json

class Gitinfo:
    
    def __init__(self): 
        pass

    def get_username(self, username):
        result = requests.get("https://api.github.com/users/{x}".format(x=username))
        result1 = json.loads(result.text)
        return result1

 
    def get_user_bio(self, result1):
        return result1['bio']
        

gituser = Gitinfo()
username = input('Enter your username: ')
result = gituser.get_username(username)
print("Bio: ", gituser.get_user_bio(result))
