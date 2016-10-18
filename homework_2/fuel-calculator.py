def fuelPrice(litres, pricePerLiter):
    max_disc = 0.25
    litres_f = float(litres.__format__(".2f"))
    pricePerLiter_f = float(pricePerLiter.__format__(".2f"))
    _dict = litres_f * 0.025
    if max_disc <= _dict:
        disc = max_disc
    elif litres_f <= 1.0:
        disc = 0.00
    else:
        disc = _dict
    price = litres_f * (pricePerLiter_f - disc)
    return float(price.__format__(".2f"))

if __name__ == '__main__':
    print(fuelPrice(10, 21.5))
