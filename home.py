from flask import render_template

# this function is passed to tutorial.py (main page)
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    print(home_page())