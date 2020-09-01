class gravity:
    mass = float(0);
    gravity = float(0);
    gravforce = float(0);
    def setmass(m):
        mass = m;
    def getmass():
        return mass;
    def getgravity():
        return gravityg;
    def getgravforce():
        return gravforce;
    def calcgravforce():
        gravforce = (-1)*mass*gravity;
