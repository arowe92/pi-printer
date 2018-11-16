from flask import Flask, request, Response
from datetime import datetime
import pystache
import pathlib

from . providers import get_providers, MessageProvider
from . import printer


def get_asset(base, name, **kargs):
    file = pathlib.Path(__file__).parent / 'data' / base / name
    with open(file, 'r') as f:
        return Response(f.read(), **kargs)


def render_template(name, data={}, meta={}):
    base = pathlib.Path(__file__).parent / 'data' / 'templates' / 'base.html'
    template = pathlib.Path(__file__).parent / 'data' / 'templates' / name
    css_file = pathlib.Path(__file__).parent / 'data' / 'styles/base.css'

    with open(css_file, 'r') as f:
        css = f.read()

    with open(template, 'r') as f:
        body = pystache.render(f.read(), data)

    with open(base, 'r') as f:
        html = pystache.render(f.read(), {
            'body': body,
            'css': css,
            'title': meta.get('title', ''),
        })

    return Response(html, content_type='text/html')


app = Flask(__name__)

# Date was last printed
last_run = None


@app.route("/print")
def run_print(*args, **kargs):
    print("Request Recieved!")
    global last_run
    once = request.args.get('once', default=0, type=int)

    print("Request Recieved!")

    day = datetime.now().day
    if once and last_run == day:
        print("Skipping, already printed")
        return ''

    providers = get_providers()
    printer.providers(*providers)

    last_run = day

    return 'success'


@app.route("/send_message", methods=['GET', 'POST'])
def run_send_message(*args, **kargs):
    name = request.form.get('name') or ''
    body = request.form.get('body') or ''
    error = ''
    success = False

    if request.method == 'POST':
        if not name or not body:
            error = 'Both fields must be entered!'
        else:
            try:
                printer.providers(MessageProvider(name, body))
                success = True
            except:
                error = 'Sorry, an error Occurred!'

    return render_template('message.html', {
        'success': success,
        'error': error,
        'name': name,
        'body': body,
    })


@app.route("/assets/styles/<string:name>")
def return_style(name):
    return get_asset('styles', name, content_type='text/css')


@app.route("/assets/scripts/<string:name>")
def return_script(name):
    return get_asset('scripts', name, content_type='text/javascript')


def start():
    app.run(host='0.0.0.0')
