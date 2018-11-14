from . providers import get_providers
from . import printer


def print_todo():
    print('generating html')
    providers = get_providers()

    print('Rendering')
    printer.providers(*providers)
