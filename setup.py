from setuptools.command.build_py import build_py
from setuptools import setup
import pathlib


class PostBuildCommand(build_py):
    def run(self):
        import sass
        path = pathlib.Path().parent / 'src/data/styles/base.scss'
        path2 = pathlib.Path().parent / 'src/data/styles/base.css'

        print("Creating sass")
        with open(path, 'rb') as f:
            scss = f.read()
            css = sass.compile_string(scss)

        with open(path2, 'wb') as f2:
            f2.write(css)
            print(css)

        build_py.run(self)


setup(
    name='todo_printer',  # Required
    version='1.0.0',  # Required
    packages=[
        'todo_printer',
        'todo_printer.providers',
    ],
    package_dir={
        'todo_printer': 'src',
        'todo_printer.providers': 'src/providers',
    },
    package_data={
        'todo_printer': [
            'data/*.css',
            'data/templates/*.html',
            'data/svg/*.svg',
        ]
    },
    include_package_data=True,
    cmdclass = { 'build_py': PostBuildCommand, },
    install_requires=[
        'pystache',
        'markdown',
        'sass',
        'python-escpos',
        'flask'
    ],

    entry_points={  # Optional
        'console_scripts': [
            'start_todo_server=todo_printer.server:start',
            'print_todo=todo_printer.functions:print_todo',
        ],
    },
)
