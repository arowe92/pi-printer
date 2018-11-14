import json
from pathlib import Path
from subprocess import Popen
import pystache
import markdown


class JSHandler():

    def __init__(self, output_file='output.png', loc='/tmp/js'):
        self.script = f'''
            var page = require('webpage').create();

            page.viewPort = {{
                width: 382,
            }};

            function render() {{
                page.render('{output_file}');
                phantom.exit();
            }}
        '''

        self.loc = loc
        self.output_file = output_file

    def run(self):
        with open(self.loc, 'w') as f:
            f.write(self.script)

        p = Popen(['phantomjs', self.loc])
        p.wait()

    def html(self, html):
        self.script += f'''
            var onLoadFinished = render;
            window.setTimeout(onLoadFinished, 3000);
            page.setContent({html}, '');
        '''

        return self

    def url(self, url):
        self.script += f'''
            page.open('{url}', render);
        '''

        return self


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

    JSHandler(output_file).html(html).run()
    return output_file


def url_to_image(url, output_file='output.png'):
    JSHandler(output_file).url(url).run()
    return output_file


def markdown_to_image(text, output_file='output.png'):
    html = markdown.markdown(text)
    return html_to_image(html, output_file)
