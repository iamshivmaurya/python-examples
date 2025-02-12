
# def triangle_area(l,h):
#     area = (1/2) * (h*l)
#     return area

# Volume of a sphere
#V=34​πr3
def cube(r):
    return r*r*r

def sphere_valume(r):
    return (4/3) * 3.14 * cube(r)

radius = int(input("Enter sphere radius in meter: "))
result = sphere_valume(radius)

print("Sphere valume : ", result ,"m3")

#l = int(input("Enter height for a triangle : ")) # 20 => "20" string
#h = int(input("Enter lenght for a triangle : "))
#area = triangle_area(l, h)
#print("Triangle Area = ", area)