
def calculator(*args, operation='sum'):

    if operation == 'sum':
        result = sum(args)
    elif operation == 'subtract':
            result = args[0] - sum(args[1:])
    elif operation == 'multiply':
            result = 1
            for num in args:
                result *= num
    elif operation == 'divide':
            result = args[0]
            for num in args[1:]:
                result /= num
    else:
            result = 'Invalid operation'

    return result
print(calculator(12,356,78,11,2, operation= 'multiply'))