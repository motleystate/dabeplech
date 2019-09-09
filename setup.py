from setuptools import setup, find_packages

setup(name="bioapi",
      version="0.0.1",
      description='Light library to perform request to different bioinformatics APIs',
      author='Kenzo-Hugo Hillion',
      author_email='kehillio@pasteur.fr',
      install_requires=[
          'requests',
          'colored'
      ],
      packages=find_packages()
)
