from flask import Flask, render_template, request
from firebase import  firebase 
import random
#import time
from datetime import datetime, timedelta
#from datetime import timedelta
import pytz
import json
import pandas as pd


app = Flask(__name__)
    

#firebaseapp = firebase.FirebaseApplication('https://test1-1ab25-default-rtdb.firebaseio.com', None)
firebaseapp = firebase.FirebaseApplication('https://test1-f1e04-default-rtdb.firebaseio.com/')
#firebaseapp = firebase.FirebaseApplication('https://flask-test-72f92-default-rtdb.firebaseio.com', None)

@app.route('/', methods=['POST'])
def home_page():
    timezone = pytz.timezone('America/New_York')
    data = firebaseapp.get("/Status", None)
    #print(data)
    pddata = {"Time": [], "Weight":[]}
    bottle_weight = 400
    for item, i in data.items():
         if 'Weight' in i and 'Time' in i:
            weight_in_oz = (i['Weight'] - bottle_weight) * 0.035
            pddata["Weight"].append(weight_in_oz)
            pddata["Time"].append(datetime.fromtimestamp(i['Time'], tz=timezone))
    df = pd.DataFrame(data=pddata)
    print(df)
    totalc = 0
    prev_date = None
    values = []
    
    for i in range(len(df)):
        timestamp = df.loc[i, 'Time']
        value = df.loc[i, 'Weight']
    
        current_date = timestamp.date()
        
        
        if current_date != prev_date  and prev_date is not None:
            values.append({ "dt": prev_date.strftime('%Y-%m-%d'), "total" :totalc})
            totalc = 0
        
 
        if i < len(df) - 1:
                next_value = df.loc[i+1, 'Weight']
                if(value > next_value):
                    difference = value - next_value
                    totalc += difference
                    #print(totalc)
                
    prev_date = current_date
    values.append({ "dt": current_date.strftime('%Y-%m-%d') , "total" :totalc})
    
    goal = 64
    lastval = values[len(values)-1]
    totc = lastval["total"]
    totc = int(totc * 100)/100
    amount_drank = round(totc/goal* 100)
    leftOver = goal-totc
    values1 = [totc, leftOver] 
    return render_template("home.html", data=values1, goal=goal, percent=amount_drank)

    # Render the HTML template with the plot data

if __name__ == '__main__':
    app.run(debug=True)