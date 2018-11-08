import pystache
from pathlib import Path

class Provider:

    template = None
    template_raw = None

    @staticmethod
    def get_template(template):
        path = Path(__file__).parent.parent / 'data' / 'templates' / f'{template}.ms.html'
        with open(path.absolute(), 'r') as f:
            return f.read()

    def get_data() -> dict:
        return {}

    def render(self) -> str:
        data = self.get_data()

        if self.template is not None:
            content = self.get_template(self.template)
        elif self.template_raw is not None:
            content = self.template_raw
        else:
            raise Exception("No template found!")

        return pystache.render(content, data)
