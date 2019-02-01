#!/usr/bin/python

class Shape:
    #parameters: area (double)
    def __init__(self, area):
        self._area = area
        
    def get_area(self):
        return self._area
    
    def display(self):
        raise NotImplementedError

class Circle(Shape):
    #parameters: area (double), radius (double)
    def __init__(self, area, radius):
        Shape.__init__(self, area)
        self._radius = radius

    def get_radius(self):
        return self._radius

    def display(self):
        print("Shape Type: Circle, Area: %d, Radius: %d")%(self._area,self._radius)

class Triangle(Shape):
    #parameters: area (double), edge_lengths ([double]), angle_degrees ([double])
    def __init__(self, area, edge_lengths, angle_degrees):
        Shape.__init__(self,area)
        self._edgelengths = edge_lengths
        self._angledegrees = angle_degrees

    def get_edge_lengths(self):
        return self._edgelengths

    def get_angle_degrees(self):
        return self._angledegrees

    def display(self):
        print("Shape Type: Triangle, Area: %d")%(self._area)
        edges = self._edgelengths
        angles = self._angledegrees
        
        for i in range(len(edges)):
            print("Edge %d: %d")%(i+1,edges[i])
        for i in range(len(angles)):
            print("Angle %d: %d degrees")%(i+1,angles[i])
        
class Square(Shape):
    #parameters: area (double), edge_size (double)
    def __init__(self, area, edge_size):
        Shape.__init__(self,area)
        self._edgelength = edge_size

    def get_edge_size(self):
        return self._edgelength

    def display(self):
        print("Shape Type: Square, Area: %d, Edge Size: %d")%(self._area,self._edgelength)


if __name__ == '__main__':
    shape1 = Circle(30.0,5.0) #not checking that these are possible values
    shape2 = Triangle(25.0,[5.0,4.0,3.0],[30.0,60.0,90.0])
    shape3 = Square(9.0,3.0)

    shapes = []
    shapes.append(shape1)
    shapes.append(shape2)
    shapes.append(shape3)

    n = len(shapes)
    for i in range(n):
        for j in range(0,n-i-1):
            if shapes[j] < shapes[j+1] :
                shapes[j], shapes[j+1] = shapes[j+1], shapes[j]

    for i in range(len(shapes)):
        shapes[i].display()
