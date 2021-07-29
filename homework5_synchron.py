import time


def factorize(*numbers):
    deviders = []
    for number in numbers:
        deviders_one_number = factorize_one_number(number)
        deviders.append(deviders_one_number)

    return deviders


def factorize_one_number(number):
    deviders_one_number = []
    for devider in range(1, number+1):
        if number % devider == 0:
            deviders_one_number.append(devider)

    return deviders_one_number


#start = time.time()
a, b, c, d, e, f, g, h = factorize(
    128, 255, 99999, 10651060, 45403940, 34534334, 23434432, 73423424)
#end = time.time()
# print(end-start)
assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
             380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

'''
administrator@Vostro-3558:/aterra/python/goit-python-web$ /usr/bin/python3.9 /aterra/python/goit-python-web/homework5.py
1.3094894886016846
administrator@Vostro-3558:/aterra/python/goit-python-web$ /usr/bin/python3.9 /aterra/python/goit-python-web/homework5.py
1.1949315071105957
administrator@Vostro-3558:/aterra/python/goit-python-web$ /usr/bin/python3.9 /aterra/python/goit-python-web/homework5.py
1.2628118991851807
administrator@Vostro-3558:/aterra/python/goit-python-web$ /usr/bin/python3.9 /aterra/python/goit-python-web/homework5.py
1.2010557651519775
administrator@Vostro-3558:/aterra/python/goit-python-web$ /usr/bin/python3.9 /aterra/python/goit-python-web/homework5.py
1.1623420715332031
'''
