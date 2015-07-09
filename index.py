import requests
import json
def byteify(input):
     if isinstance(input, dict):
         return {byteify(key):byteify(value) for key,value in input.iteritems()}
     elif isinstance(input, list):
         return [byteify(element) for element in input]
     elif isinstance(input, unicode):
         return input.encode('utf-8')
     else:
         return input

r = requests.get("https://api.github.com/repos/joeyism/node-checkout-cli/commits")
commitsArr = byteify(json.loads(r.text))
for commitsObj in commitsArr:
    print commitsObj["commit"]["committer"]["date"]
