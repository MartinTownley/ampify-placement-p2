import requests
import json

response = requests.get('https://api.ampifymusic.com/packs')

# print(type(response))
r_dict = response.json()

packsList = r_dict['packs']

# print(packsList[0])
# print(packsList[0]['genres'])

# print(r_dict['packs'][0]['genres'])
print(r_dict.get('packs'))


# packsList is a list of dictionaries, with key values as numbers 0-49.
# value of each keynumber is a dictionary with string keys such as id etc. One key is genres, whose value is a list


# search_key = 'genres'

# make a temp
# temp = list(r_dict.items())
# print(temp)

# the packs is a list
# [i for i, d in enumerate(thePacksList) if "genres" in d.keys()]


# print(response)

# print(dir(response))  # shows us atributes and methods accessible within this response object


# for key in r_dict.keys():
#    value = r_dict[key]
#    print(key, "=", value)


# now we can access these values just like any other dictionary

# iterate JSON ke-value pairs:

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'Compsci']}

# print(student['name'])

## error handling ##
# try:
#    print(student['weight'])
# except KeyError:
#    print("The student has no weight.")

# help(student.get)

# print(r_dict.get('packs'))

# this will return true for anything less than a 400 response, i.e. if there are no client or server errors.
# print(response.ok)
