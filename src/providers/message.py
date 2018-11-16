from datetime import datetime
from . util import Provider
from markdown import markdown


class MessageProvider(Provider):

    css = '''
        #message h2, #message h3{
            margin-top: 0px;
            margin-bottom: 0px;
        }
        #message p {
            text-align: left;
            font-size: 120%;
        }
        #message #from {
            font-weight: 300;
        }
        #mssage #title {
            float: left;
        }
        #message #date {
            float: right;
        }
        #message header {
            font-weight: 700;
            font-size: 125%;
            margin: 0px;
            padding: 0px;
            padding-top: 10px;
        }
    '''

    template_raw = '''
        <header>
            <span id='title'>
                Message Received
            <span>
            <span id='date'>
                {{date}}
            </span>
        </header>
        <h2>
            <span id='from'>From:</span>
            <label>{{name}}<label>
        </h2>
        <p>
            {{{body}}}
        </p>
    '''

    def __init__(self, name, body):
        self.data = {
            'name': name,
            'body': markdown(body),
            'date': datetime.now().strftime('%I:%M %p, %m/%d/%y')
        }
