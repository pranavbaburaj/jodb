import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydob", # Replace with your own username
    version="0.0.2",
    author="Pranav Baburaj",
    description="PyDOB  connector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranavbaburaj/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)