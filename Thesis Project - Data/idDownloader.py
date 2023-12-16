import requests
import time

token = "PCpHc6jmFKLzALhrxE5NJ7Tqaso3xLghZHJRPooI"  # API token
filePath = "D:\Thesis\Silver-Gold"  # filepath, edit based on your pc
getUrl = "https://ballchasing.com/api/replays"  # API url
# noOfReplays = 200
payload = {'min-rank': 'champion-1', "max-rank": "grand-champion-3",
           "count": 200, "replay-date-before": "2020-01-02T15:00:05+01:00",  "replay-date-after": "2019-01-02T15:00:05+01:00"}  # parameters for the replay
names = ["" for x in range(200)]

with open('replaynames-batch-8.txt', 'w') as f:
    for i in range(200):
        r = requests.get(getUrl, headers={'Authorization': token}, params=payload)
        a = r.json()
        # print(a['list'][i]['id'])  # the replay's ID
        f.write(a['list'][i]['id'] + ".replay" + "\n")
        filename = a['list'][i]['id'] + ".replay"  # Change the file name each time based on the replay
        names[i] = a['list'][i]['id']
        time.sleep(0.5)

for i in range(len(names)):
    getUrl = "https://ballchasing.com/api/replays/" + names[i] + "/file"  # Change the replayID everytime
    r = requests.get(getUrl, headers={'Authorization': token}, params=payload)
    time.sleep(0.5)
    with open('D:\Thesis/' + names[i]+".replay", 'wb') as f:  # Change path based on your pc
        f.write(r.content)

'''r = requests.get(getUrl, headers={'Authorization': token}, params=payload)
a = r.json()
with open('testJson3.json', 'w') as f:
    json.dump(a, f)'''
