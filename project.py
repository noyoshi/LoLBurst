#!/usr/bin/env python3

from flask import Flask, render_template, url_for, jsonify, request, session, Response
import json
import os
import collections
from helpers import *
from item_helper import *
from stat_parse import *
from base import *

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    CURR_DIR = os.getcwd()
    if os.path.isfile(CURR_DIR + "/champ1.json"):
        os.popen('rm {}/champ1.json'.format(CURR_DIR))
    if os.path.isfile(CURR_DIR + "/champ2.json"):
        os.popen('rm {}/champ2.json'.format(CURR_DIR))
    if os.path.isfile(CURR_DIR + "/item1.json"):
        os.popen('rm {}/item1.json'.format(CURR_DIR))
    if os.path.isfile(CURR_DIR + "/item2.json"):
        os.popen('rm {}/item2.json'.format(CURR_DIR))

    session['champs'] = initialize_champs()
    session['items'] = initialize_items()
    return render_template('item.html')

@app.route("/delete/<num>", methods=['POST', 'GET'])
def delete(num):
    champfile = "champ" + num + ".json"
    itemfile = "item" + num +".json"
    try:
        f = open(itemfile)
        CURR_DIR = os.getcwd()
        champion = {}
        if os.path.isfile('{}/{}'.format(CURR_DIR,champfile)):
            # Loads config file
            q = open('{}/{}'.format(CURR_DIR,champfile))
            champion = json.loads(q.read())
        INFO = json.loads(f.read())
        for searchkey in request.form.keys():
            #print(name)
            if searchkey in INFO.keys():
                del INFO[searchkey]
            #some_dict = {key: value for key,value in INFO.items() if key is not searchkey}
        with open(itemfile, 'w') as f:
            json.dump(INFO, f)
        return render_template("item.html", champ=[champion,INFO, num])
    except:
        return ("I'm a teapot", 412)


@app.route("/stats", methods=['GET', 'POST'])
def stats():
    champion1_stats, champion2_stats = stat_calc(18)
    return render_template("stats.html", stats=[champion1_stats, champion2_stats])

@app.route("/info", methods=['GET', 'POST'])
def info():
    return render_template("info.html")

@app.route("/edit/<num>", methods=['GET', 'POST'])
def edit(num):
    CURR_DIR = os.getcwd()
    name = None
    if 'Name' in request.form.keys():
        originalname = request.form['Name'].strip()
        name = originalname.replace("'","").title().replace(" ","").replace(".","")
    if name == "Wukong":
        name = "MonkeyKing"
    elif name == "JarvanIv":
        name = "JarvanIV"
    champion = {}
    champfile = "champ" + num + ".json"
    itemfile = "item" + num + ".json"
    if name:
        stats = get_champ_stats(name)
        champion = {'name': name, 'stats': stats, 'abilities': [], 'id': originalname}
        for index in range(0, 5):
            text, icon = get_champ_spell(name, index)
            champion['abilities'].append([text, icon])

        with open(champfile, 'w') as s:
            json.dump(champion,s)

    else:
        if os.path.isfile('{}/{}'.format(CURR_DIR,champfile)):
            # Loads config file
            f = open('{}/{}'.format(CURR_DIR,champfile))
            champion = json.loads(f.read())

    # Item Block
    item = None
    if 'Item' in request.form.keys():
        item = request.form['Item'].strip()
    tempItemDict = get_item_icon()
    itemDict = {}
    itemdata = {}
    if item:
        gold = tempItemDict[item]['gold']['total']
        _id = tempItemDict[item]['id']
        description = tempItemDict[item]["description"].replace("<stats>", "<stats style='color: #86D287'>")
        stats = tempItemDict[item]["stats"]
        itemDict = {'name': item, 'id': _id, 'gold': gold, 'description': description, 'stats': stats}
        if os.path.isfile('{}/{}'.format(CURR_DIR,itemfile)):
            with open(itemfile) as f:
                itemdata = json.load(f)
            if len(itemdata) < 6:
                itemdata.update({item: itemDict})
                with open(itemfile, 'w') as f:
                    json.dump(itemdata, f)
        else:
            itemdata = {item: itemDict}
            with open(itemfile, 'w') as f:
                json.dump(itemdata, f)

    else:
        if os.path.isfile('{}/{}'.format(CURR_DIR,itemfile)):
            # Loads config file
            f = open('{}/{}'.format(CURR_DIR, itemfile))
            itemdata = json.loads(f.read())
    itemdatanew = collections.OrderedDict(sorted(itemdata.items(), key=lambda x: x[1]['gold'], reverse=True))
    return render_template('item.html', champ=[champion, itemdatanew, num])

@app.route("/data/<datatype>", methods=['GET', 'POST'])
def data(datatype):
    if datatype == 'champs':
        return Response(open('champion.json').read(), mimetype='text/json')
    elif datatype == 'items':
        return Response(open('item.json').read(), mimetype='text/json')
    else:
        return ('{} data not found...'.format(datatype), 402)

@app.route("/backend", methods=['GET'])
def backend():
    key = request.args.get("key", "")
    if not key:
        return ('', 204)

    back = request.args.get("backend", "trie")
    datatype = request.args.get("datatype", "champs")
    print("key: {}, backend: {}, datatype: {}".format(key, back, datatype))
    if back == 'unsorted':
        ds = UnsortedList()
    elif back == 'sorted':
        ds = SortedList()
    elif back == "trie":
        ds = Trie()
    else:
        return ("I'm a teapot", 412)

    if datatype == 'champ':
        if not session.get('champs'):
            session['champs'] = initialize_champs()
        info = session['champs']
    elif datatype == "item":
        if not session.get('items'):
            session['items'] = initialize_items()
        info = session['items']
    else:
        return ("I'm a teapot", 412)


    ds.insert(info)
    elements = ds.search(key)

    data = []
    for e in elements:
        if datatype == 'champ':
            champ = json.load(open('champion.json'))['data'][info[e]]
            image = champ['image']['full']
            data.append({'name': e, 'image': image})
        else:
            item = json.load(open('item.json'))['data'][info[e]]
            image = item['image']['full']
            data.append({'name': e, 'image': image})

    return (jsonify(data), 200)

if __name__ == '__main__':
    app.run()


# @app.route(("/champ"), methods=['GET', 'POST'])
# def champ():
#     # Name Block
#     #print(request.path)
#     CURR_DIR = os.getcwd()
#     name = None
#     if 'Name' in request.form.keys():
#         originalname = request.form['Name'].strip()
#         name = originalname.replace(" ","").replace(".","")
#     champion = {}
#
#     if name:
#         champion = {'name': name, 'abilities': [], 'id': originalname}
#         for index in range(1, 5):
#             text, icon = get_champ_spell(name, index)
#             champion['abilities'].append([text, icon])
#
#         with open('champ1.json', 'w') as s:
#             json.dump(champion,s)
#
#
#         # if os.path.isfile('{}/champ1.json'.format(CURR_DIR)):
#         #     with open('champ1.json') as q:
#         #         champdata = json.load(q)
#         #     if len(champdata) < 2:
#         #         champdata.update({originalname: champion})
#         #         with open('champ1.json', 'w') as r:
#         #             json.dump(champdata, r)
#         # else:
#         #     champdata = {originalname: champion}
#         #     with open('champ1.json', 'w') as s:
#         #         json.dump(champdata, s)
#
#
#
#         #with open('champ1.json', 'w') as f:
#         #    json.dump(champion, f)
#     else:
#         if os.path.isfile('{}/champ1.json'.format(CURR_DIR)):
#             # Loads config file
#             f = open('{}/champ1.json'.format(CURR_DIR))
#             champion = json.loads(f.read())
#
#     # Item Block
#     item = None
#     if 'Item' in request.form.keys():
#         item = request.form['Item'].strip()
#     tempItemDict = get_item_icon()
#     itemDict = {}
#     itemdata = {}
#     if item:
#         gold = tempItemDict[item]['gold']['total']
#         _id = tempItemDict[item]['id']
#         description = tempItemDict[item]["description"].replace("<stats>", "<stats style='color: #86D287'>")
#         stats = tempItemDict[item]["stats"]
#         itemDict = {'name': item, 'id': _id, 'gold': gold, 'description': description, 'stats': stats}
#         if os.path.isfile('{}/item1.json'.format(CURR_DIR)):
#             with open('item1.json') as f:
#                 itemdata = json.load(f)
#             if len(itemdata) < 6:
#                 itemdata.update({item: itemDict})
#                 with open('item1.json', 'w') as f:
#                     json.dump(itemdata, f)
#         else:
#             itemdata = {item: itemDict}
#             with open('item1.json', 'w') as f:
#                 json.dump(itemdata, f)
#
#     else:
#         if os.path.isfile('{}/item1.json'.format(CURR_DIR)):
#             # Loads config file
#             f = open('{}/item1.json'.format(CURR_DIR))
#             itemdata = json.loads(f.read())
#     itemdatanew = collections.OrderedDict(sorted(itemdata.items(), key=lambda x: x[1]['gold'], reverse=True))
#     return render_template('item.html', champ=[champion, itemdatanew])


# @app.route("/delete_champ", methods=['POST', 'GET'])
# def delete_champ():
#     f = open("champ1.json")
#     CURR_DIR = os.getcwd()
#     item = {}
#     if os.path.isfile('{}/item1.json'.format(CURR_DIR)):
#         # Loads config file
#         q = open('{}/item1.json'.format(CURR_DIR))
#         item = json.loads(q.read())
#     INFO = json.loads(f.read())
#     for searchkey in request.form.keys():
#         if searchkey in INFO.keys():
#             del INFO[searchkey]
#     with open('champ1.json', 'w') as f:
#         json.dump(INFO, f)
#     return render_template("item.html", champ=[INFO, item])
