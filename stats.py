#from firebase import firebase
from flask import render_template
import json

# initialize firebase url
#firebase = firebase.FirebaseApplication('https://test1-f1e04-default-rtdb.firebaseio.com/', None)

# this function is passed to tutorial.py (main page)
def stats_page():
    # Logic for the stats page
    #result = firebase.get('/weights', None)

    # Define Plot Data 
    labels = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
    ]
 
    data = [0, 10, 15, 8, 22, 18, 25]
 
    # Return the components to the HTML template 
    return render_template('stat.html')
    #return render_template('stat.html', weights=result)
    #return 'Stats Page' + str(result)

if __name__ == '__main__':
    # just for debugging, print stats page info to the console
    print(stats_page())