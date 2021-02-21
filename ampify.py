import requests

response = requests.get('https://api.ampifymusic.com/packs')

# print(response)

# print(dir(response))  # shows us atributes and methods accessible within this response object

jsonResponse = response.json()
# print(jsonResponse)

# print(jsonResponse.items())

# iterate JSON ke-value pairs:
# for key, value in jsonResponse.items():
#    print(key, ":", value)

# print(jsonResponse['https://api.ampifymusic.com/packs'])


# this will return true for anything less than a 400 response, i.e. if there are no client or server errors.
print(response.ok)

print(response.headers)
