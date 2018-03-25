#!/usr/bin/env python3

from flask import Flask, render_template, url_for, jsonify, request
import json
import os
from helpers import *
from item_helper import *

app = Flask(__name__)

@app.route("/")
def index():
    if os.path.isfile('/home/silver/Projects/LoLSite/champ1.json'):
        os.popen('rm /home/silver/Projects/LoLSite/champ1.json')
    if os.path.isfile('/home/silver/Projects/LoLSite/item1.json'):
        os.popen('rm /home/silver/Projects/LoLSite/item1.json')
    return render_template('main.html')

@app.route("/load_champs", methods=['POST', 'GET'])
def load_champs():
    data = {'Apple':None, 'Derp': None}
    return jsonify(data)

@app.route("/champ", methods=['GET', 'POST'])
def champ():
    # Name Block
    name = None
    if 'Name' in request.form.keys():
        name = request.form['Name'].strip().replace(" ", "").replace("'", "")
    champion = {}
    if name:
        champion = {'name': name, 'abilities': []}
        for index in range(1, 5):
            text, icon = get_champ_spell(name, index)
            champion['abilities'].append([text, icon])
        with open('champ1.json', 'w') as f:
            json.dump(champion, f)
    else:
        if os.path.isfile('/home/silver/Projects/LoLSite/champ1.json'):
            # Loads config file
            f = open('/home/silver/Projects/LoLSite/champ1.json')
            champion = json.loads(f.read())

    # Item Block
    item = None
    if 'Item' in request.form.keys():
        item = request.form['Item'].strip()
    tempItemDict = get_item_icon()
    itemDict = {}
    if item:
        gold = tempItemDict[item]['gold']['total']
        _id = tempItemDict[item]['id']
        description = tempItemDict[item]["description"].replace("<stats>", "<stats style='color: #86D287'>")
        stats = tempItemDict[item]["stats"]
        itemDict = {'name': item, 'id': _id, 'gold': gold, 'description': description, 'stats': stats}
        with open('item1.json', 'w') as f:
            json.dump(itemDict, f)
    else:
        if os.path.isfile('/home/silver/Projects/LoLSite/item1.json'):
            # Loads config file
            f = open('/home/silver/Projects/LoLSite/item1.json')
            itemDict = json.loads(f.read())

    return render_template('main.html', champ=[champion, itemDict])


if __name__ == '__main__':
    app.run()
