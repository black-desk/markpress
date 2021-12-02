import codecs
from setuptools import setup


with codecs.open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="markpress",
    version="2.0.2",
    license_files=("LICENSE"),
    description="A fast tunnel proxy that help you get through firewalls",
    author="skywind3000",
    author_email="skywind3000@163.com",
    url="https://github.com/skywind3000/markpress",
    packages=["markpress"],
    install_requires=[
        "PySocks",
        "beautifulsoup4",
        "markdown",
        "python-wordpress-xmlrpc",
    ],
    entry_points="""
    [console_scripts]
    markpress = markpress.nextpress:main
    """,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    long_description=long_description,
)
