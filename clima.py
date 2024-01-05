import requests
from flask import Flask, request, render_template 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', temperature=None, weather_description=None, humidity=None)

@app.route('/clima', methods = ['POST'])
def clima():


   
    city = request.form.get('city')
    api_key = 'd3f6dc97bdcc3da795626dffd9ad1bab'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        lon = data['coord']['lon']
        humidity = data['main']['humidity']
        lat = data['coord']['lat']
        
        return render_template('index.html', temperature=temperature, weather_description=weather_description, lon=lon, humidity=humidity, lat=lat)
    
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template('index.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)


