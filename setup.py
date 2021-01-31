from setuptools import setup

setup(
        name='rdk_confgen',
        version='0.1',
        py_modules=['confgen'],
        install_requires=[
            'Click',
            ],
        entry_points='''
        [console_scripts]
        confgen = rdk_confgen:confgen
        ''',
        )
