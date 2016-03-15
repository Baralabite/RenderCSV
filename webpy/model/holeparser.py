from csv import reader
from model.holeentry import HoleEntry

class HoleParser:
    """
    Parses specified CSV file.
    Be warned that this function could take some time.

    TODO: Provide the ability to not load the entire file into memory when parsing
    """
    def __init__(self, filename):
        self.filename = filename
        self.holes = {}

    """
    Parses self.filename CSV
    """
    def parse(self):
        with open("data/holes.csv", "r") as csvfile:
            self.reader = reader(csvfile)
            self.reader.next()                          #Skip over the CSV header
            for row in self.reader:
                hole = HoleEntry(row)
                self.holes[hole.id] = hole

    """
    getHoles:
    Returns dictionary of all holes as HoleEntrys

    return dict{HoleEntry, ...}
    """
    def getHoles(self):
        return self.holes

    """
    getHole:
    Returns a specific HoleEntry instance from it's ID

    return HoleEntry
    """
    def getHole(self, holeID):
        return self.holes[holeID]

        """
    Returns the hole with the minimum easting
    """
    def getMinEasting(self):
        return min(self.getHoles(), key=lambda i: self.holes[i].easting)

    """
    Returns the hole with the maximum easting
    """
    def getMaxEasting(self):
        return max(self.getHoles(), key=lambda i: self.holes[i].easting)

    """
    Returns the hole with the minimum easting
    """
    def getMinNorthing(self):
        return min(self.getHoles(), key=lambda i: self.holes[i].northing)

    """
    Returns the hole with the maximum easting
    """
    def getMaxNorthing(self):
        return max(self.getHoles(), key=lambda i: self.holes[i].northing)

    """
    Returns the hole with the minimum elevation
    """
    def getMinElevation(self):
        return min(self.getHoles(), key=lambda i: self.holes[i].elevation)

    """
    Returns the hole with the maximum elevation
    """
    def getMaxElevation(self):
        return max(self.getHoles(), key=lambda i: self.holes[i].elevation)


    """
    Gets the distance between the "southmost" and "northmost" holes
    """
    def getEastingDifference(self):
        return abs(self.getMaxEasting()-self.getMinEasting())


    """
    Gets the distance between the "southmost" and "northmost" holes
    """
    def getNorthingDifference(self):
        return abs(self.getMaxNorthing()-self.getMinNorthing())

    """
    Gets the distance difference between highest and lowest holes
    """
    def getElevationDifference(self):
        return abs(self.getMaxElevation()-self.getMinElevation())