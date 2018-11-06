from setuptools import setup

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
        ]
    },
    include_package_data=True,

    install_requires=[
        'pystache',
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
