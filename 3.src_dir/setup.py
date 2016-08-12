from setuptools import setup, find_packages

setup(
    name = "demo",
    version = "0.3",
    package_dir = {'':'src'},
    packages = find_packages('src'),
    package_data = {
        #'': ['*.md'],
        'demo': ['*.md'],
        'hello': ['requirements.txt']
    },
#    include_package_data = True,
#    exclude_package_data = { 'demo': ['test.*'] },
    entry_points = {
        'console_scripts': [
            'demo = demo:main',
            'hello = hello:main',
        ],
        'ep_group': [
            'demo = demo:main',
            'hello = hello:main',
        ]
    }
)
