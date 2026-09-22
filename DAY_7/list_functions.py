#append()- Add One Element
numbers = [101, 217, 301]

numbers.append(404)

print(numbers)              #[101, 217, 301, 404]




#insert()- Add at a Specific Position
numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers)              #[10, 20, 30, 40]




#extend() — Add Multiple Elements
numbers = [10, 20, 30]

numbers.extend([40, 50, 60])

print(numbers)              #[10, 20, 30, 40, 50, 60]




#remove()- Remove by Value
numbers = [10, 20, 30, 40]

numbers.remove(30)

print(numbers)              #[10, 20, 40]



#pop() — Remove by Index
numbers = [11, 76, 87, 99]

numbers.pop(1)

print(numbers)              #[11, 87, 99]



#clear() — Remove Everything
numbers = [10, 20, 30]

numbers.clear()

print(numbers)              #[]




