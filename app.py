from flask import Flask, render_template
from data import *

app = Flask(__name__)

main_tours = dict()
i = 0
for key in tours.keys():
    i += 1
    main_tours[key] = tours[key]
    if i >= 6:
        break

@app.route('/')
def render_index():
    return render_template('index.html', title = title, subtitle = subtitle, description = description, \
                           departures = departures, main = True, tours = main_tours)

@app.route('/departures/<departure>/')
def render_dep(departure):
    dep_tours = dict()
    for key, value in tours.items():
        if tours[key]['departure'] == departure:
            dep_tours[key] = tours[key]
    return render_template('departure.html', title = title, departures = departures, main = False, \
                           tours=dep_tours, dep = departure)

@app.route('/tours/<id>/')
def render_tour(id):
    stars = ''
    for _ in range(int(tours[int(id)]['stars'])):
        stars += '★'
    return render_template('tour.html', title = title, departures = departures, \
                           tour = tours[int(id)], stars = stars, main = False, dep = tours[int(id)]['departure'])

if __name__ == '__main__':
    app.run()

