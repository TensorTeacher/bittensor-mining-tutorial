## This Tutorial Shows How to Start a Model Endpoint

1. Get a server from Runpod or Vast AI that uses the Bittensor image

2. Run:
```
apt update && apt upgrade -y
apt install sudo
```
4. Run:
```
sudo apt update && sudo apt upgrade -y && sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates && curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash - && sudo apt -y install nodejs && node -v && npm install pm2 -g && printf '\n\n' 
```
6. Pick a model from Huggingface

7. Modify the model endpoint script to use the new model:
https://github.com/TensorTeacher/endpoint-center/blob/main/model_endpoint.py

8. Copy the script to the server:
```
cat > endpoint.py
```
9. Modify the pm2.json file:
```
{
  "apps": [
     {
       "name": "s1",
       "script": "endpoint.py",
       "args": [
         "--auth_token",
         "auth_token_to_access_your_server",
         "--model_name",
         "name_on_huggingface",
         "--port",
         "port_you_want_to_use"
       ],
       "interpreter": "python",
       "env": {
         "CUDA_VISIBLE_DEVICES": "0"
       }
     },
  ]
}
```
10. Copy it to the server:

cat > pm2.json

12. Start the model inference:
pm2 start pm2.json

13. Test that it works:
```
import requests
import json

url = "http://IP_ADDRES_HERE:PORT_HERE"


messages = [{'role': 'user', 'content': "What is 2+1?"}]

headers = {"Content-Type": "application/json"}

response = requests.post(
    url, 
    data=json.dumps({"messages": messages}), 
    headers={"Content-Type": "application/json"}
)

print("Response:", response.json()["response"])
```
