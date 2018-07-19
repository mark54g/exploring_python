def invest(amount, rate, time):
    print("principal amount: ${}".format(float(amount)))
    print("anual rate of return: {}".format(float(rate)))
    for years in range(time):
        amount = amount + (amount * rate)
        print("year {}: ${}".format(years, amount))
    print()
        

invest(100, .05, 8)
invest(2000, .025, 5)
