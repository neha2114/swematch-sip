from flask import Flask, render_template
from firebase import  firebase 

app = Flask(__name__)

#firebaseapp = firebase.FirebaseApplication('https://test1-f1e04-default-rtdb.firebaseio.com', None)
firebaseapp = firebase.FirebaseApplication('https://test1-1ab25-default-rtdb.firebaseio.com', None)
print(repr(firebaseapp))


@app.route('/')
def helloworld():
    result = firebaseapp.get('/weights', None)
    print(result)
    #result = "Hello"
    return str(result)

if __name__ == 'main':
    app.run()