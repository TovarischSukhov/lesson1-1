def weather(temperature):

    if temperature <= 0:
        return("It's freezing outside")
    elif 1 <= temperature <= 15:
        return("It's cool outside")
    elif 16 <= temperature <= 25:
        return("It's warm outside")
    else:
        return("It's hot outside")

print(weather(-2))
