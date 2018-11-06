from datetime import datetime
from . util import Provider


class DateProvider(Provider):

    template_raw = '''
        <h1>
            <span id='day'>{{day}}</span>
            <span id='date'>{{date}}</span>
        </h1>
    '''

    def get_data(self) -> dict:
        now = datetime.now()

        return {
            'day': now.strftime("%A"),
            'date': now.strftime("%B %d, %Y")
        }
