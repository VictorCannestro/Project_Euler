############################################################################################################################
#
# Problem 2
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:
# 
#        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.
############################################################################################################################

def fibSum():
    # Initialize
    i = 1
    fib = [1, 2]
    evens = [2]
    tol = 4000000

    while fib[-1] < tol:
        # Generate fibonacci number
        new = fib[i] + fib[i-1]
        fib.append(new)

        # Find evens
        if new % 2 == 0:
            evens.append(new)
        i += 1

    fib.pop(-1)

    return sum(evens)

if __name__ == "__main__":
    print(fibSum())