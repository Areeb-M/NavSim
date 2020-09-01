class friction:
    coeff = float(0);
    normal = float(0);
    friction = float(0);
    def setcoeff(c):
        coeff = c;
    def getcoeff():
        return coeff;
    def getnormal():
        return normal;
    def getfriction():
        return friction;
    def calcfriction():
        friction = normal*coeff;
