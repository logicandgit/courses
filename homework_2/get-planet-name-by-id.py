def get_planet_name(id):
    # This doesn't work; Fix it!
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn",
               "Uranus", "Neptune")
    return planets[id-1]

if __name__ == '__main__':
    print(get_planet_name(3))
