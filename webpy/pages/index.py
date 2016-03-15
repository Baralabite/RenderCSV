from web import template
import web
from model.holeparser import HoleParser
from config import CSV_PATH

class index:
    def GET(self):
        self.holeParser = HoleParser(CSV_PATH)
        self.holeParser.parse()
        render = template.render('pages/')

        #TODO Make the rendering scaling not based on changing the actual raw data
        scale = 10

        canvasWidth = self.holeParser.getEastingDifference()*scale
        canvasHeight = self.holeParser.getNorthingDifference()*scale
        normalizedPointCloud = self.holeParser.normalizePointCloud(self.holeParser.getMinEasting().easting, self.holeParser.getMinNorthing().northing, 0, scale=10)
        borderSize = 40

        return render.index(canvasWidth, canvasHeight, normalizedPointCloud, borderSize)