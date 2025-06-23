import math
class Vector3D:
    def __init__(self , x, y , z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"Vector is: {self.x}i + {self.y}j + {self.z}k"

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __eq__(self , v2):
        return self.x == v2.x and self.y == v2.y and self.z == v2.z

    
    def __add__(self, other):
        return Vector3D(self.x + other.x , self.y + other.y , self.z + other.z)
    
    def __mul__(self, other):
        return Vector3D(self.x * other.x , self.y * other.y , self.z * other.z)
    
    def magnitude(self):
        return (math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2 ))
    
    def __lt__(self , other):
        return self.magnitude() < other.magnitude()
    

    def __le__(self , other):
        return self.magnitude() <= other.magnitude()

    def __gt__(self , other):
        return self.magnitude() > other.magnitude()
    
    def __ge__(self , other):
        return self.magnitude() >= other.magnitude()

    # zero vector
    @staticmethod
    def Zero():
        return Vector3D(0,0,0)
    

    #cross product
    def cross(self , v1 , v2):
        x1 = (v1.y * v2.z - v1.z * v2.y)
        x2 = (v1.x * v2.z - v1.z * v2.x)
        x3 = (v1.x * v2.y - v1.y * v2.x)
        return Vector3D(x1,x2,x3)
    
    #get item
    def get_item(self , index):
        if(index == 0):
            return self.x
        elif(index == 1):
            return self.y
        
        return self.z


v1 = Vector3D(1,1,4)
v2 = Vector3D(7,2,1)
print(v1)
print(v2)
print(v1 == v2) # eq method will be called
print(v1+v2) 
print(v1*v2)
print(v1.cross(v1 ,v2))
print(v1 < v2)
print(v1.get_item(0))

