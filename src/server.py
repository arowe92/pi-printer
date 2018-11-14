from flask import Flask, request
from datetime import datetime
from . providers import get_providers
import printer

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


@app.route("/print_markdown")
def run_print_md(*args, **kargs):
    text = request.args.get('markdown', default=0, type=int)
    printer.markdown(text)

    return 'success'


def start():
    app.run(host='0.0.0.0')
