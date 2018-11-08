from . util import Provider
from pathlib import Path
from datetime import date
import random

PRINCIPLES = [
    'Radical Inclusion',
    'Gifting',
    'Decommodification',
    'Radical Self-reliance',
    'Radical Self-expression',
    'Communal Effort',
    'Civic Responsibility',
    'Leaving No Trace',
    'Participation',
    'Immediacy',
]


class PrincipleProvider(Provider):

    template_raw = '''
        <style>
            #principles h3 {
                text-align: center;
                margin: 0px;
            }
            #principles svg {
                padding: 0px;
                margin: 0px;
                width: 50%;
            }
            #principles #svg {
                height: 140px;
            }

        </style>

        <section id='principles'>
            <div id='svg'>{{{svg}}}</div>
            <h3>{{content}}</h3>
        </section>
    '''

    def get_data(self) -> dict:
        random.seed(int(date.today().strftime("%d%m%y")))
        content = random.choice(PRINCIPLES)

        file = Path(__file__).parent.parent / f"data/svg/wick-{content.lower().replace(' ', '-')}.svg"
        with open(file, 'r') as f:
            svg = f.read()

        return {
            'content': content,
            'svg': svg,
        }
