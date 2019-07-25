from setuptools import setup, find_packages
import probable_happiness

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="probable-happiness",
    version=probable_happiness.__version__,
    author=probable_happiness.__author__,
    author_email=probable_happiness.__author_email__,
    description="A library for music apis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=probable_happiness.__url__,
    package_dir={'': '.'},
    packages=find_packages('.'),
    license='Anti 996 LICENSE',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.22.0'
    ],
)
