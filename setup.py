import setuptools

import bootstrap4c4d

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bootstrap4c4d-beesperester",
    version=bootstrap4c4d.__version__,
    author="Bernhard Esperester",
    author_email="bernhard@esperester.de",
    description="Jumpstart Cinema 4D plugin development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/beesperester/cinema4d-bootstrap",
    packages=setuptools.find_packages(exclude=[
        "tests",
        "tests.*",
        "examples",
        "examples.*"
    ]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
