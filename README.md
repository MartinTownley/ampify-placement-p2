# M Townley: Ampify Engineering Placement Test

## Part 2: Web API Parsing

### Instructions
1) Install requirements by executing the following command:
"pip install -r requirements.txt"
2) Enter "./run.sh" in the command line to run the python script "web-api-parse.py". Alternatively, enter "python3 web-api-parse.py"

(There is also an executable of the script found in "dist/")

### Process
I utilised the *Requests* module to make an HTTP request for the JSON data at https://api.ampifymusic.com/packs. The data relevant to the "packs" is stored as a Python dictionary. 

I defined a "make_genres_set" function that first creates a set, then iterates over the music packs and adds the information under the genres key to the set. The function returns the set, which eliminates duplicate entries, providing a list of the unique genres.

I then defined a "print_set_elements" function to iterate the set, and print out each individual genre.

I then defined a "print_pack_by_value" function, which takes a list and a value. If the packs list is passed in, it iterates the list of packs and determines whether the value passed in matches the pack's 'genres' key. If so, it prints the name of that pack.

The functions are called at the bottom of the script. "make_genres_set" is called on the packs_list, and "print_set_elements" is called on the result of this function, resulting in a printout of the genres.

"print_pack_by_value" is called, passing in the packs_list and the string 'hip-hop', resulting in a printout of the names of packages that have the genre attribute of 'hip-hop'.

