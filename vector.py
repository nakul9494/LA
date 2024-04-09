import math
def VectorAddition(v1, v2): 
    sum = [] 
    for i in range (len(v1)): 
        sum.append(v1[i] + v2[i]) 
    return sum


def VectorDot(v1, v2): 
    dot_product = sum(v1[i]*v2[i] for i in range(len(v1)))
    return dot_product


def VectorCross(v1, v2): 
    cross = [v1[1]*v2[2] - v1[2]*v2[1] , v1[2]*v2[0] - v1[0]*v2[2] , v1[0]*v2[1] - v1[1]*v2[0]] 
    return cross
 

def magnitude(v):
    s = 0
    for i in v:
        s += (i**2)
    return math.sqrt(s)

def VectorAngle(v1, v2):
    return math.degrees(math.acos(VectorDot(v1,v2)/(magnitude(v1) * magnitude(v2))))


def Vectordistance(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += (v1[i] - v2[i])**2
    return math.sqrt(result)


def VectorProjection(v1, v2):
    dot = VectorDot(v1, v2)
    mag = magnitude(v2) ** 2
    result = dot / mag
    projection = [a * result for a in v2]
    return projection



v1 = [] 
for i in range (0,3): 
    num = int(input("Enter values for Vector1: ")) 
    v1.append(num) 
print("Vector 1: ", v1) 

v2 = [] 
for i in range (0,3): 
    num = int(input("Enter values for Vector1: ")) 
    v2.append(num) 
print("Vector 2: ", v2) 


print(f"Vector Addition: {VectorAddition(v1, v2)}") 
print(f"Vector Dot Product: {VectorDot(v1, v2)}") 
print(f"Vector Cross Product: {VectorCross(v1, v2)}") 
print(f"Angle between Vectors: {VectorAngle(v1, v2)}")
print(f"Vector Distance: {Vectordistance(v1, v2)}")
print(f"Vector Projection: {VectorProjection(v1, v2)}")