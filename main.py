import json
#use the json file
with open('exampro.json') as f:
    d = json.load(f)
myfile = open("output.txt","a")
for doc in d:
    print("https://"+doc["docid"]+".exampro.net", end= " ")
    print(doc["documentname"], end= " ")
    print(doc["author"], end= " ")
    print(doc["datesaved"], end= " ")
    print(doc["questioncount"])
    msg = doc["documentname"]+"*"+doc["author"]+"*"+doc["datesaved"]+"*"+str(doc["questioncount"])+"*https://"+doc["docid"]+".exampro.net"
    myfile.write(msg+"\n")
myfile.close()
