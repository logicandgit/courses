import random

# TASK 1
SOLAR_SYSTEM = {"Mercury": 57.9, "Venus": 108.2, "Earth": 149.6,
                "Mars": 227.9, "Jupiter": 778.3, "Saturn": 1427.0,
                "Uranus": 2871.0, "Neptune": 4497.1}


def print_info_planet():
    planet, distance = sorted(SOLAR_SYSTEM.items())[random.randint(1, len(SOLAR_SYSTEM.keys())) - 1]
    print("Планета {pl} находится в {dist} км от Солнца".format(pl=planet, dist=distance))


if __name__ == "__main__":

    # TASK 2
    print("Выведите в консоль информацию о планетах в виде 'Планета Earth находится в ... км от Солнца'")
    for planet, distance in SOLAR_SYSTEM.items():
        print("Планета {pl} находится в {dist} км от Солнца".format(pl=planet, dist=distance))

    # TASK 3
    print("выводом планет по алфавиту")
    for planet, distance in sorted(SOLAR_SYSTEM.items()):
        # planet
        print("Планета {pl} находится в {dist} км от Солнца".format(pl=planet, dist=distance))

    # TASK 4
    print("планет по возрастанию расстояния от солнца")
    for planet, distance in sorted(SOLAR_SYSTEM.items(), key=lambda dist: dist[1]):
        # planet
        print("Планета {pl} находится в {dist} км от Солнца".format(pl=planet, dist=distance))

    # TASK 5
    print("Напишите метод, который выводит инормацию о случайной планете.")
    print_info_planet()
