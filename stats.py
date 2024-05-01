from flask import render_template, url_for
from firebase import firebase
import pandas as pd
import json

#firebaseapp = firebase.FirebaseApplication('https://test1-1ab25-default-rtdb.firebaseio.com', None)
firebaseapp = firebase.FirebaseApplication('https://test1-f1e04-default-rtdb.firebaseio.com/')
def stats_page():
    data = firebaseapp.get("/Status", None)
    print(data)
    
    pddata = {"Weight": []}
    for item, val in data.items():
        if 'Weight' in val:
            pddata["Weight"].append(val["Weight"])
    df = pd.DataFrame(data=pddata)
    
    totalc = 0
    
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    values = []
    
    for i in range(0, 69, 10):
        curr_day = df.iloc[i:i+10]
        for j in range(len(curr_day)-1):
            current_value = curr_day.iloc[j]['Weight']
            if(current_value < 0):
                current_value = abs(current_value)
            next_value = curr_day.iloc[j+1]['Weight']
            if(next_value < 0):
                next_value = abs(current_value)
            
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