import requests
import os
import io

response = requests.get("https://picsum.photos/200/300")
my_file = open("image.jpg","wb")
my_file.write(response.content)
my_file.close()
os.system("start image.jpg")