def calculate_average(numbers):
    try:
        if not numbers:
            return 0  # Handle empty list gracefully
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0  # Handle division by zero
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        return None

my_list = [10, 20, 30, 40, 50]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_zero = [10, 0, 20]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")

invalid_list = [10, "a", 20]
result = calculate_average(invalid_list)
print(f"The average is: {result}")
