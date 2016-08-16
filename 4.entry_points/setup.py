from setuptools import setup, find_packages

setup(
    name = "demo",
    version = "0.4",
    package_dir = {'':'src'},
    packages = find_packages('src'),
    entry_points = {
        'console_scripts': [
            'demo = demo:main',
            'hello = hello:main',
        ],
        'gui_scripts': [
            'demo_gui = demo:main',
            'hello_gui = hello:main',
        ],
        'setuptools.installation': [
            'eggsecutable = demo:main',
        ],
        'ep_group': [
            'demo = demo:main',
            'hello = hello:main',
        ]
    }
)
