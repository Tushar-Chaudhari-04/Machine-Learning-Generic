from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
   '''
      This function will return list of requirements
   '''
   requirements=[]
   with open(file_path) as file:
      requirements=file.readlines()
      requirements=[req.replace("\n","") for req in requirements]   

      if HYPEN_E_DOT in requirements:
         requirements.remove(HYPEN_E_DOT)

   return requirements


setup(
   name='ML_Project_Generic',
   version='0.0.1',
   author='Tushar Chaudhari',
   author_email='tushar.c8942@gmail.com',
   packages=find_packages(),
   install_requires=get_requirements('requirements.txt')
)