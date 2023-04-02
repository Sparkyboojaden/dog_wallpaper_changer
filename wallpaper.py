import requests
import json
import time
import ctypes
import os


url = "https://dog.ceo/api/breeds/image/random"

response = requests.get(url)


data = json.loads(response.content)
image_url = data["message"]
response = requests.get(image_url)

with open("dog.jpg", "wb") as f:
    f.write(response.content)

image_path = os.path.abspath("dog.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
