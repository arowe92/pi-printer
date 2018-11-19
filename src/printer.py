from escpos.printer import Usb
from functools import wraps
from . import renderer

_printer = None


def module_method(fn):

    @wraps(fn)
    def global_fn(*a, **ka):
        global _printer
        if _printer is None:
            _printer = Printer()

        return fn(_printer, *a, **ka)

    globals()[fn.__name__] = global_fn

    return fn


class Printer():

    def __init__(self, code=(0x0416, 0x5011, 0x81, 0x03)):
        self.code = code
        try:
            self.usb = Usb(*self.code)
        except Exception as e:
            print(e)

    @module_method
    def image(self, image_path):
        self.usb.image(image_path, impl='bitImageColumn')

    @module_method
    def text(self, text):
        self.usb.text(text)

    @module_method
    def html(self, html_str):
        image_file = renderer.html_to_image(html_str)
        self.image(image_file)

    @module_method
    def markdown(self, text):
        image_file = renderer.markdown_to_image(text)
        self.image(image_file)

    @module_method
    def providers(self, *providers):
        html_str = ''

        for p in providers:
            html_str += p.render()

        self.html(html_str)
