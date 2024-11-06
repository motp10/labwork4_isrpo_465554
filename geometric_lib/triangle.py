def triangle_area(a, h): 
    return a * h / 2 

def triangle_perimeter(a, b, c): 
    return a + b + c 

def is_triangle(a,b,c):
    if (a < b + c) and (b < a + c) and (c < a + b) :
        return 1
    else :
        return 0
    
def is_isosceles(a,b,c):
    if (a == b) or (b == c) or (a == c):
        return 1
    else:
        return 0

def is_equilateral(a,b,c):
    if (a == b) and (b == c):
        return 1
    else:
        return 0