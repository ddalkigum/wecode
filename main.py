def get_even():
    arr = [ number for number in  range(1, 51) if number % 2 == 0]
    print(arr)
    return arr

get_even()