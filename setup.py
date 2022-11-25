from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name="car-detection",
        version="1.0.0",
        packages=find_packages(),
        description="test package",
        url="https://github.com/infox182/engineer-ml",
        author="Ilya Skryagin"
        )