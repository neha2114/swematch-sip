from flask import Flask, render_template, request
from firebase import  firebase 
import random
#import time
from datetime import datetime, timedelta
import pytz
import json
import pandas as pd

#firebaseapp = firebase.FirebaseApplication('https://test1-1ab25-default-rtdb.firebaseio.com', None)
firebaseapp = firebase.FirebaseApplication('https://test1-f1e04-default-rtdb.firebaseio.com/')
#app = Flask(__name__)
app = Flask(__name__)

@app.route('/')
def stats_page():
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
    
    lastval = values[len(values)-1]
    totc = lastval["total"]
    totc = int(totc * 100)/100

    if len(values) > 0 :
        lastval = values[len(values) -1]
        dt = datetime.strptime(lastval["dt"], '%Y-%m-%d')
        #.date()
        num = dt.weekday()
        refdate = dt +  timedelta(days=-num)
        if num < 6:
            for k in range(num+1, 7):
                dtx = dt +  timedelta(days=k-num)
                values.append({"dt": dtx.strftime('%Y-%m-%d'), "total": 0 })
        if num > 0:
            for k in range(0,num-1 ):
                dtx = dt +  timedelta(days=k-num)
                dtStr = dtx.strftime('%Y-%m-%d')
                dtStrExists = False
                for l in range(len(values) -2, 0): 
                    if dtStr == values[l]["dt"]: 
                        dtStrExists = True
                     
                if dtStrExists == False : 
                    values.insert(k , {"dt": dtx.strftime('%Y-%m-%d'), "total": 0 })
                    
    return render_template("layout.html", data=values, total=totc)
    


if __name__ == '__main__':
    # Run the home page logic if the file is executed directly
    print(stats_page())
    
#color:linear-gradient(to bottom, #17a7c1, #1f93a8, #227f8f, #246c78, #235962)
    
#https://www.youtube.com/watch?v=B97qWOUvlnU