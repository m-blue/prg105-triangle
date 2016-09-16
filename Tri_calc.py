def is_triangle(x, y, z):
    if x > y + z:
        print("no")
    elif y > x + z:
        print("no")
    elif z > x + y:
        print("no")
    else:
        print("yes")

x = raw_input("Input a length integer: ")
y = raw_input("Input a second length integer: ")
z = raw_input("Input a third length integer: ")
is_triangle(int(x),int(y),int(z))
