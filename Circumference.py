class Circumference:

    def __init__(self, radius):
        self.radius = radius

    def circle(self):
        circumference = 2 * 3.142 * self.radius
        return circumference

    def semi_circle(self):
        circumference = 3.142 * 15 + 2 * self.radius
        return circumference

user_radius = float(input("Enter Radius: "))
object1 = Circumference(user_radius)
print("The circumference of circle is: " + str(object1.circle()))
print("The circumference of semi-circle is: " + str(object1.semi_circle()))
