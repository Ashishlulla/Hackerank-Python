n = int(input())
numbers = []
for i in range(n):
    num = input()
    numbers.append(num)
for number in numbers:
    if (number.startswith("7") or number.startswith("8") or number.startswith("9")) and (len(number)==10) and (number.isnumeric()):
        
        print("YES")
    else:
        print("NO")
