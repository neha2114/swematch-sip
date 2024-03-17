from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    goal = 60;
    oz_drank = 32
    amount_drank = round(oz_drank/goal* 100) # Percentage drank
    water_level_image = get_water_level_image(amount_drank)
    return render_template('home.html', water_level_image=water_level_image, amount_drank=amount_drank, oz_drank = oz_drank)

def get_water_level_image(amount_drank):
    # Determine the image index based on the amount drank
    image_index = round(amount_drank / 10) + 1
    if image_index < 1:
        image_index = 1
    elif image_index > 11:
        image_index = 11

    # Construct the image filename
    image_filename = f"{image_index}.png"
    return image_filename

if __name__ == '__main__':
    app.run(debug=True)
