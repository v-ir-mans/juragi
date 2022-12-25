# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from flask import render_template, request
import json
from datetime import datetime
from db import db_manager
from flask import jsonify
from order import getOrder

DB=db_manager(r"data\main.db")


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/order')
def order():
    Presents=DB.getAllPresents()
    Obol, Opres, Ocycles=getOrder(Presents)

    if Obol:
        presents_and_owners=[(op.word, op.parent_num) for op in Opres ]
    else:
        presents_and_owners="Nava"
    return {"Status":Obol, "Cycles":Ocycles, "Order":presents_and_owners}

@app.route('/get_presents')
def getP():
    Presents=DB.getWordByID(request.cookies["id"])    
    return json.dumps(Presents)

@app.route('/gen_id')
def genID(): 
    return DB.createID()

@app.route('/addPresent',methods = ['POST'])
def present():
    id=request.cookies["id"]
    ran_word=DB.getRandomWord()
    print(ran_word)
    
    DB.pinNum(ran_word["Num"])
    DB.addPresent(ran_word["Word"],ran_word["Num"],id)

    return json.dumps(ran_word)

@app.route('/removePresent',methods = ['POST'])
def removePresent():
    print(0)
    num=request.form["num"]
    if num.isnumeric():
        num=int(num)

    allowed_num=DB.getWordByID(request.cookies["id"])
    allowed_num=[i[1] for i in allowed_num]


    if num in allowed_num:
        DB.removePresentByNum(num)
    return ":)"






# main driver function
if __name__ == '__main__':
    app.run(debug=True)