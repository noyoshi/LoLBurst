#!/usr/bin/env python3

import json
import requests
from bs4 import BeautifulSoup as soup
import re
import sys
import os
import time

version = "8.8.1"

def open_json(PATH='champ_info.json'):
    f = open(PATH)
    return f

def parse_html(string):
    #regex = re.compile('<.*>')
    i = 0
    return_str = ""
    while(i < len(string)):
        s = string[i]
        if s == '<':
            i += 1
            while string[i] != '>':
                i += 1
            i += 1
        if i < len(string):
            return_str += string[i]
        i += 1
    return return_str

def replace_vars(string, effect_list, var_list, LEVEL=1):
    LEVEL = LEVEL -1
    return_str = ""
    i = 0
    while(i < len(string)):
        s = string[i]
        if s == '{':
            i = i + 3
            type_ = string[i]
            if type_ == 'e':
                i += 1
                try:
                    index = int(string[i])
                except:
                    pass
                # NEED TO CHANGE BASED ON ABILITY LEVEL
                try:
                    return_str += str(effect_list[index][LEVEL])
                except:
                    pass
            else:
                i += 1
                type_ += string[i]
                found = False
                if var_list:
                    for v in var_list:
                        if v["key"] == type_:
                            return_str += ''.join([str(x) for x in v["coeff"]])
                            return_str += " " + v["link"]
                            found = True
                            break
                    if found:
                        pass
                    elif type_[0] == 'f':
                        # The effect is in the effect list
                        index = int(type_[1])
                        return_str += str(effect_list[index][LEVEL])
                        for v in var_list:
                            if v["key"][1] == str(index):
                                return_str += v["link"]
                                break

            i += 3
        if i < len(string):
            if string[i] != '}':
                return_str += string[i]
        i += 1
    return return_str


def get_spell(champ='Katarina', SPELL=1):
    f = open_json()
    INFO = json.loads(f.read())

    CHAMP_DICT = INFO["data"] # Dict with champ name key
    if "'" in champ:
        champ = champ.replace("'","")
        if champ != "RekSai" and champ != "KogMaw":
            champ = champ[0] + champ[1:].lower()
        CHAMP_DATA = CHAMP_DICT[champ]
    else:
        CHAMP_DATA = CHAMP_DICT[champ]
    SPELLS = CHAMP_DATA["spells"]
    PASSIVE = CHAMP_DATA["passive"]
    PASSIVEINFO = {}
    PASSIVEINFO["name"] = PASSIVE["name"]
    PASSIVEINFO["tooltip"] = PASSIVE["description"]
    PASSIVEINFO["image"] = PASSIVE["image"]["full"]
    RETURN_DICT = { 0: PASSIVEINFO, 1:{}, 2: {}, 3:{}, 4:{}}
    for i, spell in enumerate(SPELLS):
        RETURN_DICT[i+1]["name"] = spell["name"]
        # effects in order of when they are mentioned in the tooltip
        RETURN_DICT[i+1]["effects"]  = spell["effect"]
        RETURN_DICT[i+1]["tooltip"] = spell["tooltip"]
        if 'vars' in spell.keys():
            RETURN_DICT[i+1]["vars"] = spell["vars"]
        else:
            RETURN_DICT[i+1]["vars"] = None
        img_d = spell["image"]
        RETURN_DICT[i+1]["location"] = [img_d["sprite"].replace("spell", "").replace(".png", ""), img_d["x"], img_d["y"]]
        #RETURN_DICT[i+1]["image"] = spell["image"]["full"]



    return RETURN_DICT[SPELL], CHAMP_DICT


def get_champ_spell(champ='Katarina', SPELL_INDEX=1, SPELL_LEVEL=3):
    spell, CHAMP_DICT = get_spell(champ, SPELL_INDEX)
    CURR_DIR = os.getcwd()
    if SPELL_INDEX >= 1:
        tooltip = replace_vars(spell["tooltip"], spell["effects"], spell["vars"], SPELL_LEVEL)
        tooltip = tooltip.replace("spelldamage", "Ability Power").replace("bonusattackdamage", "Bonus Attack Damage").replace("attackdamage", "Base Attack Damage")

        # loc = spell["location"]
        # x = loc[1]
        # y = loc[2]
        # num = loc[0]
        #temp = {1: "Q", 2: "W", 3: "E", 4: "R"}
        # q = open('champ_info.json')
        path = CHAMP_DICT[champ]["spells"][SPELL_INDEX-1]["image"]["full"]
        if not os.path.isfile(CURR_DIR + "/static/spell_icons/" + path):
            os.popen("wget -P {} https://ddragon.leagueoflegends.com/cdn/{}/img/spell/{}".format("static/spell_icons/", version, path))
            time.sleep(0.3)
        return tooltip, "spell_icons/" + path
        #return tooltip, get_icon(num, x, y)
    else:
        if not os.path.isfile(CURR_DIR + "/static/spell_icons/" + spell["image"]):
            os.popen("wget -P {} https://ddragon.leagueoflegends.com/cdn/{}/img/passive/{}".format("static/spell_icons/", version, spell["image"]))
        return spell["tooltip"], "spell_icons/" + spell["image"]

# def get_champ_spell(champ='Katarina', SPELL_INDEX=1, SPELL_LEVEL=3):
#     spell = get_spell(champ, SPELL_INDEX)
#     if SPELL_INDEX >= 1:
#         tooltip = replace_vars(spell["tooltip"], spell["effects"], spell["vars"], SPELL_LEVEL)
#         tooltip = tooltip.replace("spelldamage", "Ability Power").replace("bonusattackdamage", "Bonus Attack Damage").replace("attackdamage", "Base Attack Damage")
#
#         loc = spell["location"]
#         x = loc[1]
#         y = loc[2]
#         num = loc[0]
#         return tooltip, get_icon(num, x, y)
#     else:
#         return spell["tooltip"], "http://ddragon.leagueoflegends.com/cdn/8.6.1/img/passive/{}".format(spell["image"])

def download_icons(version):
    for n in range(1, 15):
        URL = "http://ddragon.leagueoflegends.com/cdn/{}/img/sprite/spell{}.png".format(version,n)
        os.popen('wget -P static/spell_icons/ {}'.format(URL))
        time.sleep(2)
        os.popen("convert -crop 10x4@ +repage +adjoin static/spell_icons/spell{}.png  static/spell_icons/spell{}_%d.png ".format(n, n))


def get_icon(SPELLNUM=5, x=432, y=96):
    x = int(x)
    y = int(y)
    n = (((x/48)+1) + ((y/48)*10)) - 1
    if n > 37:
        SPELLNUM = str(int(SPELLNUM) + 1)
        n = n - 38
    ICON = "spell_icons/spell{}_{}.png".format(SPELLNUM, str(int(n)))
    # if not os.path.isfile(ICON):
    #     download_icons(SPELLNUM)
    return ICON

def get_champ_stats(name):
    FILE = open_json()
    FILE_NEW = json.loads(FILE.read())
    return FILE_NEW["data"][name]["stats"]

if __name__ == '__main__':
    download_icons()
    l = "QWER"
    i = 0
    for NUM in [1,2,3,4]:
        print(l[i], " ")
        print(get_champ_spell(sys.argv[1], NUM, 3))
        i += 1
        print()
