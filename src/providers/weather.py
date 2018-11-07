
from weather import Weather, Unit
from . util import Provider


class WeatherProvider(Provider):

    template_raw = '''
        <div id='weather'>
            <span id='status'>
                {{text}},
            </span>
            <span id='temp'>{{low}}°↓ {{high}}↑°</span>
            <!-- <i class='wi wi-day-{{status}}'></i> -->
        </div>
    '''

    def get_data(self) -> dict:
        weather = Weather(unit=Unit.FAHRENHEIT)
        location = weather.lookup_by_location('austin')
        return {
            'high': location.forecast[0].high,
            'low': location.forecast[0].low,
            'text': location.forecast[0].text,
            'status': location.forecast[0].text.lower().replace(' ', '-')
        }
