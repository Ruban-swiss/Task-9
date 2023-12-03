my_list = [10, "hello", 5, "world", 3.14, "Python"]

result = list(map(lambda x: isinstance(x, (int, str)), my_list))

print(result)
