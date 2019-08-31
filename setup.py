import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cosmologger",
    version="0.1.0",
    author="SamHDev",
    author_email="sam02h.huddart@gmail.com",
    description="A Nicely formatted Logger for the Cosmo Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamHDev/cosmologger/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
)