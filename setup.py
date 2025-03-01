from setuptools import find_packages, setup

HYPEN_E_DOT = "-e ."

def get_req(file_path) :  
    requirement = []
    with open(file_path, 'r') as file_obj:  
        requirement = file_obj.readlines()
        requirement = [req.strip() for req in requirement]  

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement

setup(
    name='mlproject',
    version='1.0',  
    author='Gihan',
    author_email='gihannemindra@gmail.com',
    packages=find_packages(),  
    install_requires=get_req('requirements.txt')     
)
