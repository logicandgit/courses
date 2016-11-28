# -*- coding: utf-8 -*- 
def show_me(instname):
    element = sorted(instname.__dict__.keys())
    if len(element) == 1:
        substring = element[0]
    else:
        substring = ', '.join(element[:-1])
        substring = '{} and {}'.format(substring, element[-1])
    return "Hi, I'm one of those {}s! Have a look at my {}.".format(
        instname.__class__.__name__,
        substring
    )

if __name__ == '__main__':
    class Vehicle:
        def __init__(self, seats, wheels, engine):
            self.seats = seats
            self.wheels = wheels
            self.engine = engine


    porsche = Vehicle(2, 4, 'Gas')
    print show_me(porsche)

    class Planet:
        def __init__(self, moon):
            self.moon = moon
    earth = Planet('moon')

    print show_me(earth)
