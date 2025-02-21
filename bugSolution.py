def my_function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle the error appropriately

result = my_function(10, 0) # Returns 0
result2 = my_function(10,2) # Returns 5.0