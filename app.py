from flask import Flask, render_template, request


app = Flask(__name__)


def kelvin_to_fahrenheit(temp_kelvin):
    temp_kelvin = main_data["temp"]
    temp_fahrenheit = temp_in_kelvin * 9/5 - 459.67
    return temp_fahrenheit

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/weather")
def display_weather():
    return render_template("weather_form.html")


@app.route('/weather_results', methods=["GET"])
def weather_results_page():
    users_city = request.args.get('city')

    params = {
        'q':users_city,
        'appid' : d418aaba4e9cf886d4e98d9b56a738b8
    }
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)
    response_json = response.json()
    
    main_data = response_json["main"]
    temp_in_kelvin = main_data["temp"]
    temp_in_farenheit = temp_in_kelvin *9/5 - 459.67
    print("the temperature is" + str(temp_in_kelvin) + "in kelvin.")
    return render_template("/weather_results.html", city=city, temperature=int(temp_fahrenheit))
    

    # if not r.status_code == 200:
    #     print("error")
    # results = r.json()
    # city = results['name']
    # temp = kelvin_to_farenheit(results['main']['temp'])
    # return render_template('weather_results.html', city=city, temp=temp)





if __name__ == '__main__':
    app.run(debug=True)

