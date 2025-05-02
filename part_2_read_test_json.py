import json
import test_data

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    ### Begin Add Code Here ###
    #Loop through the json_data
    for game_name in json_data:
        game_data = json_data[game_name]
        game_system = game_data['game']
        game_year = game_data['launch year']
        game_title = game_data['title']
        g = test_data.Game(game_title, game_system, game_year)
        game_library.add_game(g)
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
json_file = open("data/game_library.json")
#Use the json module to load the data from the file
json_data = json.load(json_file)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
library = make_game_library_from_json(json_data)
#Print out the resulting GameLibrary data using print()
print(library)
### End Add Code Here ###
