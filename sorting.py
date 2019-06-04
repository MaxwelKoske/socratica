# Alkaline earth metals
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
print(earth_metals)
earth_metals.sort()
print('The sorted list: ', earth_metals)
earth_metals.sort(reverse=True)
print('Sorted in reverse order:', earth_metals)

"""
format: = (name, radius, density, distance from Sun)
Radius: Radius at equator in kilometers
Density: Average density in g/cm^3
Distance from Sun: Avg. distance to sun in AUs
1 Astronomical unit = Average distance of Earth to sun
"""


planets = [
	("Mercury", 2440, 5.43, 0.395),
	("Venus", 6052, 5.24, 0.723),
	("Earth", 6378, 5.52, 1.000),
	("Mars", 3396, 3.93, 1.530),
	("Jupiter", 71492, 1.33, 5.210),
	("Saturn", 60268, 0.69, 9.551),
	("Uranus", 25559, 1.27, 19.213),
	("Neptune", 24764, 1.64, 30.070)
	]
planets.sort()
print(planets)
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)
density = lambda x: x[2]
planets.sort(key=density)
print(planets)


#help(list.sort)
#help(sorted)

sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)

data = (7,2,5,6,1,3,9,10,4,8)
print(sorted(data))# returns a sorted list

#Sort a String
print(sorted("Alphabetical"))


