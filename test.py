import requests

BASE = "http://127.0.0.1:5000/"
data = [{"likes": 20, "name": 'video 2', "views": 2000}, {"likes": 30, "name": 'video 3', "views": 3000}, {"likes": 40, "name": 'video 4', "views": 4000}]
for i in range(len(data)):
    response = requests.put(BASE + f"video/" + str(i), data[i])
    print(response.json())

input('enter')
response = requests.get(BASE + "video/10")
print(response)