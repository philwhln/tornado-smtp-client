# tornado-smtp-client's setup.py

from distutils.core import setup
setup(
    name = "tornado-smtp-client",
    package_dir = {'': 'src'},
    packages = ["tornado", "tornado.smtp", "tornado.smtp"],
    version = "0.1.0",
    description = "Asynchronous SMTP client for Python's Tornado web framework.",
    author = "Phil Whelan",
    author_email = "phil123@gmail.com",
    url = "https://github.com/philwhln/tornado-smtp-client",
    download_url = "https://github.com/philwhln/tornado-smtp-client/zipball/master",
    keywords = ["tornado", "smtp", "email", "client"],
    classifiers = [],
    long_description = """\
Asynchronous SMTP client for Python's Tornado web framework.

Originally taken from https://gist.github.com/1358253

Also see Tornado : http://www.tornadoweb.org/
"""
)
