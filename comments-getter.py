import requests
import pprint
import json
idVideo = "lwop_SAaXmM"
apiKey = "AIzaSyDjPvcDLS7pOLG-qg03hheDYommlXMX4Ls"
url = 'https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId='+ idVideo +'&key=' + apiKey + '&maxResults=100'
print(url)

resp = requests.get(url)
data = resp.json()
# file = open("data.json", "w")
# file.write(json.dumps(data))
# print("File Written")
comments = data['items']
for comment in comments:
    print(comment['snippet']['topLevelComment']['snippet']['textDisplay'])