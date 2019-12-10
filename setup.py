import setuptools
from io import open

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyyandextranslateapi",
    version="1.2",
    author="Radif rtix Tazetdinov",
    author_email="radif.tazetdinov@mail.ru",
    description="Python library for Yandex Translate API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rtix/pyYandexTranslateAPI",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
