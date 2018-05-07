#!/usr/bin/env python3

import os
import json
from helpers import download_icons
import time
version = "8.8.1"

CURR_DIR = os.getcwd()

# Need to get this data from website
#API_KEY = "RGAPI-54f45bbd-2fd7-443d-940d-00f860eb5378"
#URL = "https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&version={}&champListData=all&tags=all&dataById=false&api_key={}".format(version,API_KEY)
#if API_KEY and not os.path.isfile(CURR_DIR +"/champ_info.json"):
#    os.popen("wget {} -O champ_info.json".format(URL))

if not os.path.isfile(CURR_DIR + "/champ_info.json"):
    os.popen("unzip champ_info.zip")

# Gets json files
if not os.path.isfile(CURR_DIR + "/champion.json"):
    os.popen("wget https://ddragon.leagueoflegends.com/cdn/{}/data/en_US/champion.json".format(version))
if not os.path.isfile(CURR_DIR + "/item.json"):
    os.popen("wget https://ddragon.leagueoflegends.com/cdn/{}/data/en_US/item.json".format(version))

time.sleep(1)
champ_list = open("champion.json")
champ_list = json.loads(champ_list.read())
for champ in champ_list["data"].keys():
    if not os.path.isfile(CURR_DIR + "/static/champ_icons/" + champ + ".png"):
        os.popen("wget -P {} https://ddragon.leagueoflegends.com/cdn/{}/img/champion/{}.png".format("static/champ_icons/", version, champ))


item_list = open("item.json")
item_list = json.loads(item_list.read())

for item in item_list["data"].keys():
    if not os.path.isfile(CURR_DIR + "/static/item_icons/" + item + ".png"):
        os.popen("wget -P {} https://ddragon.leagueoflegends.com/cdn/{}/img/item/{}.png".format("static/item_icons/", version, item))

if not os.path.isdir(CURR_DIR + "/static/spell_icons"):
    os.popen("mkdir static/spell_icons")
    download_icons(version)
