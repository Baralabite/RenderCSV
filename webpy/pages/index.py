from web import template
from model.holeparser import HoleParser
from config import CSV_PATH

class index:
    def GET(self, name):
        self.holeParser = HoleParser(CSV_PATH)
        self.holeParser.parse()

        render = template.render('pages/')
        print(self.holeParser.getEastingDifference())
        print(self.holeParser.getNorthingDifference())
        return render.index(name, 400, 400)
        #return "Hello World!"