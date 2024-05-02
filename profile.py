from flask import render_template, url_for
import pandas as pd
import json

def profile_page():
    return render_template("calc.html")