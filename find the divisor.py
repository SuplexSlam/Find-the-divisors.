'''
I came across this problem in code war and I had fun time creating and coding it. Just enter a number and it
will return an array with all the integer's divisor out the it's divisor from smallest to largest. Try entering a prime number too.
'''

user_input = int(input("➡➡➡➡➡➡: Enter a number below. \n➡➡➡➡➡➡: "))

def divisor(num):
    div = []
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                div.append(i)
        return div



def prime(num):
    flag = False

    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                flag = True
                break
    if num < 0:
        return "➡➡➡➡➡➡: Please enter a positive number."
    elif num == 0:
        return f"➡➡➡➡➡➡: {num} is rational, whole, integer and real number. Some say it's natural number too but it's debatable ¯\_(ツ)_/¯"
    elif num == 1:
        return f"➡➡➡➡➡➡: {num} is a number, a single entity. Remember {num} is not a whole number since it has only one divisor"

    else:
        if num == 69:
            return f"( ͡° ͜ʖ ͡°): {num} eh?? ( ͡° ͜ʖ ͡°) Well the divisors are: {sorted(divisor(num))}"   # added this special case for the number 69. huehuehue
        elif flag:
            return f"➡➡➡➡➡➡: The divisor of {num}: {sorted(divisor(num))}"
        else:
            return f"➡➡➡➡➡➡: {num} is a prime number.  A prime number is a whole number with exactly two integral divisors, 1 and itself i.e. {num}"


print(prime(user_input))


