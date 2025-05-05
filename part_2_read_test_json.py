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
        game_system = game_data['platform']
        game_year = game_data['game year']
        game_title = game_data['title']
        game_platform_year = game_data['platform year']
        g = test_data.Game(game_title, game_system, game_year, game_platform_year)
        #Add that Game object to the game_library
        game_library.add_game(g)
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
