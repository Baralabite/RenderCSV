from model.holeparser import HoleParser
from webhandler import WebHandler
from config import CSV_PATH
import sys

#Stops python from creating pyc (bytecode) files
sys.dont_write_bytecode


"""
Base class of the application.
Inits/starts everything else.

TODO I need to cache the CSV data, rather than processing it every GET request.
Code for it is commented out in the Application class, because I haven't figured
out a way to reference it in the pages/index.py class.
"""
class Application:
    def __init__(self):
        #self.holeParser = HoleParser(CSV_PATH) TODO
        self.webHandler = WebHandler()

    """
    Called on start of application
    """
    def start(self):
        #self.holeParser.parse() TODO
        self.webHandler.start()

if __name__ == "__main__":
    app = Application()
    app.start()