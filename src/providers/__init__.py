from . date import DateProvider
from . weather import WeatherProvider
from . todo import TodoProvider
from . principles import PrincipleProvider


def get_providers():
    return [
        DateProvider(),
        WeatherProvider(),
        TodoProvider(),
        PrincipleProvider(),
    ]
