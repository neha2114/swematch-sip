from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def loading_page():
    return 'Hi'
 
@app.route('/home/')
def home_world():
    import home
    return home.home_page()


@app.route('/stats/')
def stats_page():
    import stats
    return stats.stats_page()

if __name__ == '__main__':
    app.run(debug=True)