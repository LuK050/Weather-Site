import pyowm
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError
        
        
class Weather:
    global owm
    owm = pyowm.OWM('603aecbf06c971a53dd23cecd56daac6')
    get_default_config()['language'] = 'ru'


    def get_weather(city):
        global owm
        
        try:
            weather = owm.weather_manager().weather_at_place(city).weather
            
            temperature = weather.temperature('celsius')['temp']
            wind = weather.wind()['speed']
            humidity = weather.humidity
            detailed_status = weather.detailed_status
            
            return {"temperature": temperature, "wind": wind, "humidity": humidity, "detailed_status": detailed_status}
        
        except NotFoundError:
            return None
        
        