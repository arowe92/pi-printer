from datetime import datetime
from . util import Provider
from markdown import markdown


class MessageProvider(Provider):

    css = '''
        #message h2#from {
            float: clear;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        #message #body {
            text-align: left;
            font-size: 130%;
            padding-bottom: 20px;
            border-bottom: 1px solid black;
        }
        #message #title {
            float: left;
        }
        #message #date {
            float: right;
        }
        #message header {
            font-weight: 700;
            font-size: 120%;
            margin: 0px;
            padding: 0px;
            padding-top: 10px;
        }
    '''

    template_raw = '''
        <header>
            <span id='title'>
                Message Received
            </span>
            <span id='date'>
                {{date}}
            </span>
        </header>
        <h2 id='from'>
            <span>From:</span>
            <label>{{name}}</label>
        </h2>
        <div id='body'>
            {{{body}}}
        </div>
    '''

    def __init__(self, name, body):
        self.data = {
            'name': name,
            'body': markdown(body),
            'date': datetime.now().strftime('%I:%M %p, %m/%d/%y')
        }
