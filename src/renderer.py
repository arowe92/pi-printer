import json
from pathlib import Path
from subprocess import Popen

import pystache


def get_js(html, output_file):
    return f'''
        var page = require('webpage').create();

        page.viewPort = {{
            width: 382,
        }};

        var onLoadFinished = function() {{
            console.log('rendering to {output_file}');
            page.render('{output_file}');
            phantom.exit();
        }};

        window.setTimeout(onLoadFinished, 3000);

        page.setContent({html}, '');
    '''


# Template for Page
template = """
    <html>
        <head>
            <style>
                {{{css}}}
            </style>
        </head>
        <body>
            {{{body}}}
        </body>
    </html>
"""


def html_to_image(html: str, output_file='output.png'):
    # Inject HTML into template
    with open(Path(__file__).parent / 'data' / 'main.css', 'r') as f:
        html = pystache.render(template, {
            'css': f.read(),
            'body': html
        })

    # Convert to json string for injecting into jsa
    html = json.dumps(html)

    with open('/tmp/js', 'w') as f:
        JS = get_js(html, output_file)
        f.write(JS)

    p = Popen(['phantomjs', '/tmp/js'])
    p.wait()
