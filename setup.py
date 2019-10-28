from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
from setuptools import setup

setup(
     name='PackageName',
     version='0.1.0',
     author='An Awesome Coder',
     author_email='aac@example.com',
     packages=['socket_cli'],
     scripts=['bin/script1','bin/script2'],
     url='http://pypi.python.org/pypi/PackageName/',
     license='LICENSE.txt',
     description='An awesome package that does something',
     long_description=open('README.md').read(),
     install_requirements = [
         'click >= 7.0',
         'prompt_toolkit>=2.0.6',
     ],
 )
