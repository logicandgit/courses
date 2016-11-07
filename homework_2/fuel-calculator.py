def fuelPrice(litres, pricePerLiter):
    max_disc = 0.25
    litres_f = float(litres)
    pricePerLiter_f = float(pricePerLiter)
    t_dict = litres_f * 0.025
    if max_disc <= t_dict:
        disc = max_disc
    elif litres_f <= 1.0:
        disc = 0.00
    else:
        disc = t_dict
    price = litres_f * (pricePerLiter_f - disc)
    return float(price.__format__(".2f"))

if __name__ == '__main__':
    print(fuelPrice(10, 21.5))
