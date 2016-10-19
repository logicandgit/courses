def multi_summ(number):
    if not (str(number).isdigit()):
        return "ONLY digit"
    summ = 0
    multi = 1
    for i in str(number):
        summ += int(i)
        multi *= int(i)
    return summ, multi

if __name__ == "__main__":
    print(multi_summ(1234))
