import requests
import json

response = requests.get('https://api.ampifymusic.com/packs')

response_dict = response.json()

dict_str = json.dumps(response_dict, indent=2)  # make data readable

packs_list = response_dict['packs']

## Sort response into set of genres ##


def make_genres_set(input_list):
    genres_set = set()

    for pack in packs_list:
        pack_genre = pack['genres'][0]
        # genres_list.append(pack_genre)
        genres_set.add(pack_genre)

    return genres_set

## Print a list of all the genres ##


def print_set_elements(input_set):
    for element in input_set:
        print(element)

# Print out a list of all the packs in the genre 'hip-hop':


def print_pack_by_value(input_list, value):
    for sub in input_list:
        if value in sub['genres'][0]:
            print(sub['name'])


### Function calls ###
print("GENRES:")
print_set_elements(make_genres_set(packs_list))

print('')
print("PACKS OF GENRE 'HIP-HOP:")
print_pack_by_value(packs_list, 'hip-hop')

#genres_set = make_genres_set(packs_list)
#genres_dict = dict.fromkeys(genres_set, [])
