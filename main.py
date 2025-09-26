def baggage_fee(weight: int, length: int):
    if weight < 0 or weight > 50 or length < 0 or length > 200:
        return "Invalid"
    elif weight == 0 or length == 0:
        return 0
    elif weight <= 20 and length <= 100:
        return 0
    elif weight <= 20 and length <= 200:
        return 10
    elif weight <= 50 and length <= 100:
        return 20
    else:
        return 30
