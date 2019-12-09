import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyyandextranslateapi",
    version="1.1",
    author="Radif rtix Tazetdinov",
    author_email="radif.tazetdinov@mail.ru",
    description="Implementation of Yandex.Translate API as a Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rtix/pyYandexTranslateAPI",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
