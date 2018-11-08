from . providers import get_content
from . renderer import html_to_image
from . import printer


def print_todo():
    print('generating html')
    html = get_content()

    print('Rendering')
    html_to_image(html, 'output.jpg')

    print('printing...')
    printer.image('output.jpg')
