from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("app_requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name="monitor",
    description="Data collection for CPU metrics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.1",
    packages=find_packages(),
    install_requires=requirements,
)
