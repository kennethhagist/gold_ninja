from flask import Flask, flash, render_template, request, redirect, session, Markup
import random
import datetime
app = Flask(__name__)
app.secret_key = "secretsecret543210"

session={}
session['gold']=None
session['event']=None

def randomNum(start, end):
    num = random.randrange(start, end)
    return num


def addEvent(num, building):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if building == 'casino':
        if num<0:
            session['event'].append('Entered a casino and lost ' +str(num)+ 'gold... Ouch.. ' + '('+str(timestamp)+')')

        else:
            session['event'].append('Entered a casino and won ' +str(num)+ ' gold! ' + '('+str(timestamp)+')')
    else:
        session['event'].append('Earned ' +str(num)+ ' from the '+building+'! ' + '('+str(timestamp)+')')

@app.route('/')
def index():
    if session['gold']==None:
        session['gold']=0
    if session['event']==None:
        session['event']=[]
    return render_template("gold.html", gold = session['gold'], events = session['event'])

@app.route('/process_money', methods=['POST'])
def gold():
    if request.form['building']=='farm':
        goldEarned = randomNum(10,21)
        session['gold'] +=goldEarned
        addEvent(goldEarned, 'farm')
    elif request.form['building']=='cave':
        goldEarned = randomNum(5,11)
        session['gold'] +=goldEarned
        addEvent(goldEarned, 'cave')
    elif request.form['building']=='house':
        goldEarned = randomNum(2,6)
        session['gold'] +=goldEarned
        addEvent(goldEarned, 'house')
    elif request.form['building']=='casino':
        goldEarned = randomNum(-50,51)
        session['gold'] +=goldEarned
        addEvent(goldEarned, 'casino')

    return redirect('/')


app.run(debug=True)
