from flask import render_template, url_for
from firebase import firebase
import pandas as pd
import json
import plotly
import plotly.express as px

firebaseapp = firebase.FirebaseApplication('https://test1-1ab25-default-rtdb.firebaseio.com', None)
#firebaseapp = firebase.FirebaseApplication('https://test1-f1e04-default-rtdb.firebaseio.com/')
def stats_page():
    data = firebaseapp.get("/weights", None)
    #print(data)
    pddata = {"ts": [], "reading":[]}
    for item in data:
       pddata["reading"].append( item["reading"])
       pddata["ts"].append(item["ts"])
    df = pd.DataFrame(data=pddata)
    totalc = 0
    
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    values = []
    
    #for index, row in df.iterrows():
    #  print(row['reading'])
    
    for i in range(0, len(df), 100):
        curr_day = df.iloc[i:i+100]
        for j in range(len(curr_day)-1):
            current_value = curr_day.iloc[j]['reading']
            next_value = curr_day.iloc[j+1]['reading']
            
            if(current_value > next_value):
                difference = current_value - next_value
                totalc += difference
                
        values.append(totalc)   
        totalc = 0
    return render_template("layout.html", labels=days, values=values)


if __name__ == '__main__':
    # Run the home page logic if the file is executed directly
    print(stats_page())
    
#color:linear-gradient(to bottom, #17a7c1, #1f93a8, #227f8f, #246c78, #235962)
    
#https://www.youtube.com/watch?v=B97qWOUvlnU