def test(*args):
    print(args)


def factorial(n, m=1):  # n! = 1 * ... * n
    if n == 0:
        return 1
    m = factorial(n - 1)
    return (n * m)


number = int(input('Wellcome! Insert your number: '))
while number < 0:
    number = int(input('Invalid value. Your number must be > 0. Try again: '))
print('Factorial of', number, 'equals', factorial(number))
#ryad = [0, 0, 0, 0, 0]
#for i in range(5):
#    num = int(input())
#    ryad[i] = (factorial(num))
#test(factorial(num))
#test(input(), *ryad, 'hi', (5 < 0))
