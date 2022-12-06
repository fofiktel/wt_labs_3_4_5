
from cryptography.fernet import Fernet
import requests
import json

key = b'raTleA9iB8Nl4-hQb4wn7LYU_i909VCHfT50GFVcfdk='

with open('data.json', 'r') as read_file:
    data = json.dumps(json.load(read_file))


fernet = Fernet(key)
encMessage = fernet.encrypt(data.encode())

req = requests.get(f'http://127.0.0.1:8000/lab_4/encrypt/?data={encMessage.decode()}')
print(req.json())

