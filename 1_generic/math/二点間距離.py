import math
def distance(x1,y1,x2,y2):
    x = pow(abs(x1-x2),2)
    y = pow(abs(y1-y2),2)
    return math.sqrt(x+y)