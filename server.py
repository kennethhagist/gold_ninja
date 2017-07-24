from flask import Flask, render_template, request, redirect, session, flash
import random
import datetime
from datetime import date
app = Flask(__name__)
app.secret_key = 'SecretGoldFarm'

def randint(start,end):
    num = random.randint(start,end)
    return num

@app.route('/')
def index():
    try:
        session['booty']
    except:
        session['booty'] = 0
    try:
        session['activity']
    except:
        session['activity'] = ''
    return render_template("index.html")


@app.route('/process_money', methods=['post'])
def process_money():
    print "Gold mining..."
    found = 0
    treasure_chest =''
    ts = datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")
    landmark = request.form['building']     #landmark = worksite, building = vault
    if landmark == 'farm':
        print "farm gold mission"
        found = random.randint(10,20)
        print "found= ", found
        treasure_chest += "You entered a farm and labored {} golds {}".format(found,ts)
    elif landmark == 'cave':
        print "cave gold mission"
        found = random.randint(5,10)
        print "found= ", found
        treasure_chest += "You entered a cave and mined {} golds {}".format(found,ts)
    elif landmark == 'house':
        print "house gold mission"
        found = random.randint(2,5)
        print "found= ", found
        treasure_chest += "You entered a house and stole {} golds {}".format(found,ts)
    elif landmark == 'casino':
        print "casino gamble mission"
        found = random.randint(-50,50)
        print "found= ", found
        if found < 0:
            treasure_chest += "You entered the casino and gambled away all {} of your golds. You're a degenerate {}".format(found,ts)
        else:
            treasure_chest += "Avast, you be rich matey! go spend all {} of your golds on rum and girls {}".format(found,ts)
    else:
        print "You be lost in the Bermuda Triangle matey! Sail true by the north star"

    try:
        session['booty'] += found
    except:
        session['booty'] = found
    try:
        session['activity'] += treasure_chest + '\n'
    except:
        session['activity'] = treasure_chest + '\n'

    return redirect('/')


app.run(debug=True)


#<!-- <div id="log"> -->
    #<!-- {% for index in range(len(session['activity'])-1, -1) %} -->
        #<!-- <p> {{ session['activity'][idx] }} </p> -->
    #<!-- {% endfor %} -->
#<!-- </div> -->
