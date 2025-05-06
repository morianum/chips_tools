from cc_classes import CCLevelPack, CCLevel, CCMapTitleField, CCMapHintField, CCEncodedPasswordField
import json
from cc_dat_utils import write_cc_level_pack_to_dat

#Part 3

#Load your custom JSON file
json_file = open("data/level_set.json")
#Use the json module to load the data from the file
json_data = json.load(json_file)
#Print out the resulting GameLibrary data using print()
print(json_data)

#Convert JSON data to CCLevelPack
def make_CCLevelPack(json_data):
    pack = CCLevelPack()
    for level in json_data["levels"]:
        newLevel = CCLevel()
        newLevel.level_number = level['levelNumber']
        newLevel.time = level['time']
        newLevel.num_chips = level['chipNumber']
        newLevel.upper_layer = level['upperLayer']
        newLevel.optional_fields.append(CCMapTitleField(level["mapTitle"]))
        newLevel.optional_fields.append(CCMapHintField(level["mapHint"]))
        newLevel.optional_fields.append(CCEncodedPasswordField(level["encodedPass"]))
        pack.add_level(newLevel)
    return pack
pack = make_CCLevelPack(json_data)

#Save converted data to DAT file
write_cc_level_pack_to_dat(pack, "/Users/m.tayao/Desktop/tworld/data/level_set.dat")