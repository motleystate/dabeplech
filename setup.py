from setuptools import setup, find_packages

exec(open('dabeplech/version.py').read())

setup(
    name="dabeplech",
    version=__version__,  # noqa
    description='Light library to perform request to different bioinformatics APIs',
    author='Kenzo-Hugo Hillion',
    author_email='kehillio@pasteur.fr',
    install_requires=[
        'pydantic==1.5.1',
        'requests==2.23.0',
        'colored==1.4.2',
        'beautifulsoup4==4.9.1'
    ],
    packages=find_packages()
)
