from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

def stats_page():

    df = pd.DataFrame({
        "Day": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "Water Intake": [64, 36, 50, 45, 30, 19, 61]
    })

    days = df['Day']
    water = df['Water Intake']

    graph = px.bar(df, x=days, y=water
                   , color_discrete_sequence=['#17A7C1']*len(df),
                   width=1000, height=750,
                   range_y=[0,64])
    
    graph.update_layout(
        plot_bgcolor='#FEF8F8',
        font=dict(
            family="Literata",
            size=24,  # Set the font size here   
        )
    )
    
    graphJSON = json.dumps(graph, cls =plotly.utils.PlotlyJSONEncoder)
    
    return render_template("layout.html", graphJSON=graphJSON)

if __name__ == '__main__':
    # Run the home page logic if the file is executed directly
    print(stats_page())
    
#color:linear-gradient(to bottom, #17a7c1, #1f93a8, #227f8f, #246c78, #235962)
    
#https://www.youtube.com/watch?v=B97qWOUvlnU