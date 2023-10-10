from setuptools import find_packages,setup
from typing import List
HYPER_EDOT="-e ."

def get_requrements(file_path:str)->list[str]:
    # This function will return the list of requrements
    requrements=[]
    with open(file_path) as file_obj:
        requrements=file_obj.readlines()
        requrements=[req.replace("\n","") for req in requrements]
        if HYPER_EDOT in requrements:
            requrements.remove(HYPER_EDOT)

    return requrements
setup(
    
    
name='ML-project-ALL',
version='0.0.1',
author='Tushar Thokdar',
author_email='tusharthokdarp@gmail.com',
packages=find_packages(),
install_requrements=get_requrements("requrements.txt")
)