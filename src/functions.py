from . providers import PROVIDERS
from . renderer import html_to_image
from . import printer


def print_todo(providers=None):
    if providers is None:
        providers = PROVIDERS

    print('generating html')
    html = ''
    for p in PROVIDERS:
        html += p().render()

    html_to_image(html, 'output.jpg')
    print('printing...')
    printer.image('output.jpg')
