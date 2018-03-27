#!/usr/bin/env python3

from flask import Flask, render_template, url_for, jsonify, request
import json
import os
import collections
from helpers import *
from item_helper import *

app = Flask(__name__)

@app.route("/")
def index():
    CURR_DIR = os.getcwd()
    if os.path.isfile(CURR_DIR + "/champ1.json"):
        os.popen('rm {}/champ1.json'.format(CURR_DIR))
    if os.path.isfile(CURR_DIR + "/item1.json"):
        os.popen('rm {}/item1.json'.format(CURR_DIR))
    return render_template('item.html')

@app.route("/load_champs", methods=['POST', 'GET'])
def load_champs():
    data = {'Apple':None, 'Derp': None}
    return jsonify(data)

@app.route("/execute", methods=['POST', 'GET'])
def execute():
    f = open("item1.json")
    CURR_DIR = os.getcwd()
    champion = {}
    if os.path.isfile('{}/champ1.json'.format(CURR_DIR)):
        # Loads config file
        q = open('{}/champ1.json'.format(CURR_DIR))
        champion = json.loads(q.read())
    INFO = json.loads(f.read())
    for searchkey in request.form.keys():
        #print(name)
        if searchkey in INFO.keys():
            del INFO[searchkey]
        #some_dict = {key: value for key,value in INFO.items() if key is not searchkey}
    with open('item1.json', 'w') as f:
        json.dump(INFO, f)
    return render_template("item.html", champ=[champion,INFO])

@app.route("/delete_champ", methods=['POST', 'GET'])
def delete_champ():
    f = open("champ1.json")
    CURR_DIR = os.getcwd()
    item = {}
    if os.path.isfile('{}/item1.json'.format(CURR_DIR)):
        # Loads config file
        q = open('{}/item1.json'.format(CURR_DIR))
        item = json.loads(q.read())
    INFO = json.loads(f.read())
    for searchkey in request.form.keys():
        if searchkey in INFO.keys():
            del INFO[searchkey]
    with open('champ1.json', 'w') as f:
        json.dump(INFO, f)
    return render_template("item.html", champ=[INFO, item])

@app.route("/stats", methods=['GET', 'POST'])
def stats():
    return render_template("stats.html")

@app.route("/info", methods=['GET', 'POST'])
def info():
    return render_template("info.html")
    
@app.route("/champ", methods=['GET', 'POST'])
def champ():
    # Name Block
    CURR_DIR = os.getcwd()
    name = None
    if 'Name' in request.form.keys():
        originalname = request.form['Name'].strip()
        name = originalname.replace(" ","").replace(".","")
    champion = {}
    champdata = {}
    if name:
        champion = {'name': name, 'abilities': [], 'id': originalname}
        for index in range(1, 5):
            text, icon = get_champ_spell(name, index)
            champion['abilities'].append([text, icon])




        if os.path.isfile('{}/champ1.json'.format(CURR_DIR)):
            with open('champ1.json') as q:
                champdata = json.load(q)
            if len(champdata) < 2:
                champdata.update({originalname: champion})
                with open('champ1.json', 'w') as r:
                    json.dump(champdata, r)
        else:
            champdata = {originalname: champion}
            with open('champ1.json', 'w') as s:
                json.dump(champdata, s)



        #with open('champ1.json', 'w') as f:
        #    json.dump(champion, f)
    else:
        if os.path.isfile('{}/champ1.json'.format(CURR_DIR)):
            # Loads config file
            f = open('{}/champ1.json'.format(CURR_DIR))
            champdata = json.loads(f.read())

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
        if os.path.isfile('{}/item1.json'.format(CURR_DIR)):
            with open('item1.json') as f:
                itemdata = json.load(f)
            if len(itemdata) < 6:
                itemdata.update({item: itemDict})
                with open('item1.json', 'w') as f:
                    json.dump(itemdata, f)
        else:
            itemdata = {item: itemDict}
            with open('item1.json', 'w') as f:
                json.dump(itemdata, f)

    else:
        if os.path.isfile('{}/item1.json'.format(CURR_DIR)):
            # Loads config file
            f = open('{}/item1.json'.format(CURR_DIR))
            itemdata = json.loads(f.read())
    itemdatanew = collections.OrderedDict(sorted(itemdata.items(), key=lambda x: x[1]['gold'], reverse=True))
    return render_template('item.html', champ=[champdata, itemdatanew])

if __name__ == '__main__':
    app.run()
