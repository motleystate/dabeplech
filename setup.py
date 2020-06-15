from setuptools import setup, find_packages

exec(open('bioapi/version.py').read())

setup(
    name="bioapi",
    version=__version__,  # noqa
    description='Light library to perform request to different bioinformatics APIs',
    author='Kenzo-Hugo Hillion',
    author_email='kehillio@pasteur.fr',
    install_requires=[
        'pydantic==1.5.1',
        'requests==2.23.0',
        'colored==1.4.2'
    ],
    packages=find_packages()
)
