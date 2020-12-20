import setuptools
import os

with open(f"{os.path.dirname(os.path.realpath(__file__))}/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QualtricsData",
    version="0.0.1",
    author="Ashish Mehta",
    author_email="ashm@stanford.edu",
    description="A package to read and preprocess Qualtrics Data",
    long_description=long_description,
    url="https://github.com/amehtaSF/QualtricsData",
    packages=setuptools.find_packages(),
    license = "License :: OSI Approved :: MIT License",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
