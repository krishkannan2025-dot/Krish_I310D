def calculate_volume_of_circle(radius):
    pi = 3.142
    volume = (4/3) * pi * radius * radius * radius
    return volume

radius1 = 30
volume1 = calculate_volume_of_circle(radius1)
print(f"The volume of a sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calculate_volume_of_circle(radius2)
print(f"The volume of a sphere with radius {radius2} is: {volume2}")
