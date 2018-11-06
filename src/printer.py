from escpos.printer import Usb
from functools import wraps


class Printer():
    instance = None

    def __init__(self, code=(0x0416, 0x5011)):
        self.code = code
        self.usb = Usb(*self.code)

    @staticmethod
    def method(fn):

        @wraps(fn)
        def _wrapper(*args, **kargs):
            global instance
            if Printer.instance is None:
                Printer.instance = Printer()

            return fn(Printer.instance.usb, *args, **kargs)

        return _wrapper


@Printer.method
def image(p, image_path):
    p.image(image_path, impl='bitImageColumn')


@Printer.method
def text(p: Usb, text: str) -> None:
    p.text(text)
