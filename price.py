# Task 1

def get_summ(one, two, delimiter=' '):
    	return str(one).upper() + str(delimiter) + str(two).upper()
sum_string = get_summ ('Learn', 'python', " - ")
print(sum_string)


# Task 2

def format_price(price):
    price = int(price)
    return "Price: " + str(price) + " rub." # попробуй разобраться и сделать через .format()
display_price = format_price(56.24)
print(display_price)


# def discounted(price, discount, max_discount=50):
    # price = abs(float(price))
    # discount = abs(float(discount))
    # max_discount = abs(float(discount))#снова дискаунт а не макс дискаунт 
    # if max_discount > 99:
    #    raise ValueError("Max discount cannot be more then 99%")
    #if discount >= max_discount:
        #price_with_discount = price
    #else:
        #price_with_discount = price - (price * discount / 100)
    #return price_with_discount

#print(discounted(100, 50, max_discount=100)) # давай ещё форматер сделаем красивый? Из серии «только сегодня скидка х и вместо н цена будет всего а»
# и общую функцию, а-ля сформируй ценник


