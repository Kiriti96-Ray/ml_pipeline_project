from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n", "") for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)


setup(
    name="ml_pipeline_project",
    version="0.0.1",
    description="Machine learning pipeline project",
    author="Kiriti Ray Choudhury",
    author_email="kiritiroychoudhury@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
