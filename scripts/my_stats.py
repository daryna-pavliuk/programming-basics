def average(numbers):
    if len(numbers) < 1:
        return "Error: function 'average' is missing an argument"
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def minimum(numbers):
    if len(numbers) < 1:
        return "Error: function 'minimum' is missing an argument"
    smallest = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest