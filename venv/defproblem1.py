import math



def getCircleArea(radius):
    return math.pow(radius,2) * math.pi

def getDounutArea(r1,r2):

    area1 = getCircleArea(r1)
    area2 = getCircleArea(r2)

    return  abs(area1-area2)



if __name__ == "__main__":
    result = getDounutArea(5,10)
    print(result)