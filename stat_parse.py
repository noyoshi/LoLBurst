#!/usr/bin/env python3

import json
import os

def stat_json_file(file):
    CURR_DIR = os.getcwd()
    if not os.path.isfile(CURR_DIR + "/" + file):
        return None
    c1 = open(file)
    c1_dict = json.loads(c1.read())
    return c1_dict

def compile_item_stats(curr_dict):
    stats = {}
    for key in curr_dict.keys():
        for key2 in curr_dict[key]["stats"].keys():
            val = curr_dict[key]["stats"][key2]
            stats[key2] = stats.get(key2, 0) + val
    return stats


def stat_calc(level):
    champ1_dict = stat_json_file('champ1.json')
    champ2_dict = stat_json_file('champ2.json')
    item1_dict = stat_json_file('item1.json')
    item2_dict = stat_json_file('item2.json')
    champ_stats1 = {}
    champ_stats2 = {}
    item_stats1 = {}
    item_stats2 = {}
    if champ1_dict:
        champ_stats1 = champ1_dict["stats"]
    if champ2_dict:
        champ_stat2 = champ2_dict["stats"]
    if item1_dict:
        item_stats1 = compile_item_stats(item1_dict)
    if item2_dict:
        item_stats2 = compile_item_stats(item2_dict)
    if champ_stats1:
        for key in champ_stats1.keys():
            if key.endswith("perlevel") and not key.startswith("attackspeed"):
                temp = key[0:-8]
                champ_stats1[temp] = champ_stats1[temp] + (champ_stats1[key] * (level-1))
        champ_stats1["attackspeed"] = (0.625/(1+champ_stats1["attackspeedoffset"])) * (1 + (champ_stats1["attackspeedperlevel"]*(level-1)/100 ))
    if champ_stats2:
        for key in champ_stats2.keys():
            if key.endswith("perlevel") and not key.startswith("attackspeed"):
                temp = key[0:-8]
                champ_stats2[temp] = champ_stats2[temp] + (champ_stats2[key] * (level-1))
        champ_stats2["attackspeed"] = (0.625/(1+champ_stats2["attackspeedoffset"])) * (1 + (champ_stats2["attackspeedperlevel"]*(level-1)/100 ))
    if item_stats1 and champ_stats1:
        for key in item_stats1.keys():
            temp = key.lower()
            temp = temp[0:-3]
            #if temp.endswith("pool"):
        #        temp = temp[:-4]
            temp = temp.replace("movementspeed","movespeed").replace("pool","").replace("critchance","crit")

            if temp.startswith("flat"):
                champ_stats1[ temp[4:] ] = champ_stats1.get(temp[4:],0) + item_stats1[key]
            elif temp.startswith("percent"):
                stat = temp[7:]
                if stat != "attackspeed":
                    champ_stats1[stat] = champ_stats1[stat]*(1+item_stats1[key])
                else:
                    champ_stats1["attackspeed"] = (0.625/(1+champ_stats1["attackspeedoffset"])) * (1 + ((champ_stats1["attackspeedperlevel"]*(level-1) ) + item_stats1[key])/100)
        for key in champ_stats1.keys():
            champ_stats1[key] = round(champ_stats1[key],3)
    # if item_stats2 and champ_stats2:
    #     for key in item_stats2.keys():
    #         temp = key.lower()
    #         temp = temp[0:-3]
    #         if temp.endswith("pool"):
    #             temp = temp [:-4]
    #         if "movementspeed" in temp:
    #             temp = temp.replace("movemenetspeed", "movespeed")
    #         if temp.startswith("flat"):
    #             champ_stats2[ temp[4:] ] += item_stats2[key]
    #         elif temp.startswith("percent"):
    #             stat = temp[7:]
    #             if stat != "attackspeed":
    #                 champ_stats2[stat] = champ_stats2[stat]*(1+item_stats2[key])
    #             else:
    #                 champ_stats2["attackspeed"] = (0.625/(1+champ_stats2["attackspeedoffset"])) * (1 + (champ_stats2["attackspeedperlevel"]*(level-1) ) + item_stats2[key])
    print(champ_stats1)
    return champ_stats1, champ_stats2



    # "FlatHPPoolMod":0,"rFlatHPModPerLevel":0,"FlatMPPoolMod":0,"rFlatMPModPerLevel":0,"PercentHPPoolMod":0,"PercentMPPoolMod":0,"FlatHPRegenMod":0,"rFlatHPRegenModPerLevel":0,
    #"PercentHPRegenMod":0,"FlatMPRegenMod":0,"rFlatMPRegenModPerLevel":0,"PercentMPRegenMod":0,"FlatArmorMod":0,"rFlatArmorModPerLevel":0,"PercentArmorMod":0,
    #"rFlatArmorPenetrationMod":0,"rFlatArmorPenetrationModPerLevel":0,"rPercentArmorPenetrationMod":0,"rPercentArmorPenetrationModPerLevel":0,"FlatPhysicalDamageMod":0,
    #"rFlatPhysicalDamageModPerLevel":0,"PercentPhysicalDamageMod":0,"FlatMagicDamageMod":0,"rFlatMagicDamageModPerLevel":0,"PercentMagicDamageMod":0,"FlatMovementSpeedMod":0,
    #"rFlatMovementSpeedModPerLevel":0,"PercentMovementSpeedMod":0,"rPercentMovementSpeedModPerLevel":0,"FlatAttackSpeedMod":0,"PercentAttackSpeedMod":0,
    #"rPercentAttackSpeedModPerLevel":0,"rFlatDodgeMod":0,"rFlatDodgeModPerLevel":0,"PercentDodgeMod":0,"FlatCritChanceMod":0,"rFlatCritChanceModPerLevel":0,
    #"PercentCritChanceMod":0,"FlatCritDamageMod":0,"rFlatCritDamageModPerLevel":0,"PercentCritDamageMod":0,"FlatBlockMod":0,"PercentBlockMod":0,"FlatSpellBlockMod":0,
    #"rFlatSpellBlockModPerLevel":0,"PercentSpellBlockMod":0,"FlatEXPBonus":0,"PercentEXPBonus":0,"rPercentCooldownMod":0,"rPercentCooldownModPerLevel":0,"rFlatTimeDeadMod":0,
    #"rFlatTimeDeadModPerLevel":0,"rPercentTimeDeadMod":0,"rPercentTimeDeadModPerLevel":0,"rFlatGoldPer10Mod":0,"rFlatMagicPenetrationMod":0,"rFlatMagicPenetrationModPerLevel":0,
    #"rPercentMagicPenetrationMod":0,"rPercentMagicPenetrationModPerLevel":0,"FlatEnergyRegenMod":0,"rFlatEnergyRegenModPerLevel":0,"FlatEnergyPoolMod":0,"rFlatEnergyModPerLevel":0,
    #"PercentLifeStealMod":0,"PercentSpellVampMod":0
