"""
HoleEntry

id (int):           ID of hole
easting (float):    Easting of hole
northing (float):   Northing of hole
elevation (float):   Elevation of hole

Data structure for easily accessing specific hole information
"""
class HoleEntry:
    def __init__(self, row):
        try:
            self.id = int(row[0])
        except TypeError:
            self.id = None

        try:
            self.easting = float(row[1])
        except TypeError:
            self.easting = None

        try:
            self.northing = float(row[1])
        except TypeError:
            self.northing = None

        try:
            self.elevation = float(row[1])
        except TypeError:
            self.elevation = None