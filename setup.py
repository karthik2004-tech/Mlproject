from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:

setup(
    name='mlproject',
    version='0.0.1',
    author='karthik',
    author_email='karthiktelukutla@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements.txt('requirements.txt')

)