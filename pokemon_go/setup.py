from setuptools import setup, find_packages

setup(
    name = "pokemon_go",
    version = "0.1",
    package_dir = {'':'src'},
    packages = find_packages('src'),
    entry_points = {
        'console_scripts': [
            'poke_pkg = poke_pkg:main',
            'poke_std = poke_std:main',
        ]
    },
    install_requires = [
        "pokemon_3in1>=0.1",
        "pokemon_2in1>=0.1",
    ]
)
