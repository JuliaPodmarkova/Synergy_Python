numbers = input().split(' ')
count = 0

for num in numbers:
    if num.count('6') > 0:
        if num.count('8') > 0:
            continue
        else:
            count += 1
    elif num.count('8') > 0:
        count += 1

print(count)# Напишите здесь свой код :-)
