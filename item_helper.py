import json

def get_item_icon():
    f = open("item_8.6.json")
    INFO = json.loads(f.read())
    output = {}
    for key, value in INFO["data"].items():
        # If on Summoner Rift
        if INFO["data"][key]["maps"]["11"]:
            temp_dict = {}
            for key1 in INFO["basic"].keys():
                if key1 in INFO["data"][key].keys():
                    temp_dict[key1] = INFO["data"][key][key1]
                else:
                    temp_dict[key] = ""
            temp_dict["id"] = key
            # print(INFO["data"][key])
            output[ INFO["data"][key]["name"] ] = temp_dict
    return output

def get_item_dict():
    f = open("item_8.6.json")
    INFO = json.loads(f.read())
    output = {}
    for key, value in INFO["data"].items():
        # If on Summoner Rift
        if INFO["data"][key]["maps"]["11"]:
            output [ INFO["data"][key]["name"] ] = "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/" + INFO["data"][key]["image"]["full"]
    with open('item_icons.json', 'w') as f:
        json.dump(output, f)

def get_champ_dict():
    f = open("champ_info.json")
    INFO = json.loads(f.read())
    output = {}
    for key, value in INFO["data"].items():
        output [ INFO["data"][key]["name"] ] = "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/item/" + INFO["data"][key]["image"]["full"]
    with open('champ_icons.json', 'w') as f:
        json.dump(output, f)
