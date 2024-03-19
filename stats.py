from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

def stats_page():

    df = pd.DataFrame({
        "Days": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "Water Intake": [64, 36, 50, 45, 30, 19, 61]
    })

    days = df['Days']
    water = df['Water Intake']

    graph = px.bar(df, x=days, y=water
                   , color_discrete_sequence=['#17A7C1']*len(df),
                   animation_frame=days,
                   animation_group=days,
                   range_y=[0,64])
    
    graphJSON = json.dumps(graph, cls =plotly.utils.PlotlyJSONEncoder)
    
    return render_template("layout.html", graphJSON=graphJSON)

if __name__ == '__main__':
    # Run the home page logic if the file is executed directly
    print(stats_page())
    
#https://www.youtube.com/watch?v=B97qWOUvlnU