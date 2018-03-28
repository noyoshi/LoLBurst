#!/usr/bin/env python3

import os
import json
from helpers import download_icons
import time
version = "8.6.1"

CURR_DIR = os.getcwd()

API_KEY = "RGAPI-64037db2-ec12-496c-a512-19ad2eb53ae3"
URL = "https://na1.api.riotgames.com/lol/static-data/v3/champions?locale=en_US&version=8.6.1&champListData=all&tags=all&dataById=false&api_key={}".format(API_KEY)
if API_KEY and not os.path.isfile(CURR_DIR +"/champ_info.json"):
    os.popen("wget {} -O champ_info.json".format(URL))
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
