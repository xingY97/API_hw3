from flask import Flask, render_template, request


app = flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/weather")
def display_weather():
    return render_template("weather_form.html")


@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')

    params = {
        'q':users_city,
        'appid' : d418aaba4e9cf886d4e98d9b56a738b8
    }
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)

    if not r.status_code == 200:
        print("error")
    results = r.json()
    city = results['name']
    temp = kelvin_to_farenheit(results['main']['temp'])
    return render_template('weather_results.html', city=city, temp=temp)

def kelvin_to_farenheit(k):
    results = 1.8 * (k-273) + 32
    return int(results)



if __name__ == '__main__':
    app.run()

