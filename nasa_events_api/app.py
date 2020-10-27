import json
import requests as req

url = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'

resp = req.get(url)

data = json.loads(resp.text)

count = 0

userInput = input('ID: ')

for key, val in data.items():
    if(key == "events"):
        for event in val:
            for title, value in event.items():
                if title == "categories":
                    for a in value:
                        for b,data in a.items():
                            if(b == "id"):
                                id = data
                                if(id == int(userInput)):
                                    count += 1
                                    print(event)
                                    print('\n')
                            if(b == "title"):
                                title = data


print("Number of events: ", count)
