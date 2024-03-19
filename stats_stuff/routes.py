from stats_stuff import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

@app.route('/stats/')
def index():

    df = px.read_excel('TextData.xlsx') 

    title = 'Weekly Stats'
    days = df['Days']
    water = df['Water Intake']

    graph = px.bar(df, x='Days', y='Water Intake'
                   , color_discrete_sequence=['blue']*len(df),
                   animation_frame=days,
                   animation_group=days,
                   title=title,
                   range_y=[0,64])

    return render_template("layout.html", graph1JSON=graph1JSON)
