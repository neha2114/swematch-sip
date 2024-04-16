import base64
from io import BytesIO
from flask import Flask, render_template
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/')
def home_page():
    goal = 60;
    oz_drank = 32
    amount_drank = round(oz_drank/goal* 100) # Percentage drank
    water_level_image = get_water_level_image(amount_drank)

    size_of_groups = [22, 78]
    colors = ['#EDF3F9', '#4D7495']  # Example colors

    # Create a pie chart
    plt.figure()
    plt.pie(size_of_groups, colors=colors)
    my_circle = plt.Circle((0,0), 0.7, color='white')
    plt.gcf().gca().add_artist(my_circle)

    # Save the plot to a BytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Encode the plot as a base64 string
    plot_data = base64.b64encode(buffer.read()).decode('utf-8')

    # Render the HTML template with the plot data

    return render_template('home.html', water_level_image=water_level_image, amount_drank=amount_drank, oz_drank = oz_drank, plot_data=plot_data)

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

