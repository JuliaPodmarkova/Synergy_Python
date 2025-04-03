# Задача 2. Списковый синхрон

list1 = [1, 2, 3, 4, 5]
list2 = [10, 9, 8,7, 6, 5]
list3 = []
min_count = 4
c = 0

if len(list1) >= min_count and len(list2) >= min_count:
    for i in range(len(list1)):
        n = (list1[i] * list2[c])
        list3.append(n)
        c += 1
        if c == len(list2):
            c = 0
    print(list3[:min_count:])
elif len(list1) > len(list2):
    a = len(list2)
    d = list1[:a:]
    b = list2[:a:]
    d.extend(b)
    print(d)
    list3 = [x * y for x, y in zip(d[::2], d[1::2])]
    print(list3)
elif len(list1) < len(list2):
    a = len(list1)
    d = list1[:a:]
    b = list2[:a:]
    d.extend(b)
    print(d)
    list3 = [x * y for x, y in zip(d[::2], d[1::2])]
    print(list3)
