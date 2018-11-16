import pystache
from pathlib import Path

class Provider:

    template = None
    template_raw = None
    css = ''

    base_template = '''
    <section class='provider' id='{{id}}'>
        {{{content}}}
        <style>{{{css}}}</style>
    </section>
    '''

    @staticmethod
    def get_template(template):
        path = Path(__file__).parent.parent / 'data' / 'templates' / f'{template}.ms.html'
        with open(path.absolute(), 'r') as f:
            return f.read()

    def get_data(self) -> dict:
        if hasattr(self, 'data'):
            return self.data
        else:
            return {}

    def render(self) -> str:
        data = self.get_data()

        if self.template is not None:
            content = self.get_template(self.template)
        elif self.template_raw is not None:
            content = self.template_raw
        else:
            raise Exception("No template found!")

        # Render content
        html = pystache.render(content, data)

        # insert into baseline template
        return pystache.render(self.base_template, {
            'id': self.__class__.__name__.lower().replace('provider', ''),
            'content': html,
            'css': self.css,
        })

    @staticmethod
    def render_all(providers):
        html = ''

        for p in providers:
            html += p.render()

        return html
