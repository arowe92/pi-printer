from . date import DateProvider
from . weather import WeatherProvider
from . todo import TodoProvider
from . principles import PrincipleProvider

PROVIDERS = [
    DateProvider,
    WeatherProvider,
    TodoProvider,
    PrincipleProvider,
]


def get_content():
    html = ''

    for p in PROVIDERS:
        html += p().render()

    return html
