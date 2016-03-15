import web

"""
Imports the page class files
TODO: Import automatically based on the contents of urls
"""
from pages.index import index

"""
Defines url data structure
"""
urls = (
    '/(.*)', 'index'
)

class WebHandler:
    def __init__(self):
        self.app = web.application(urls, globals())
        web.config.debug = False

    def start(self):
        self.app.run()