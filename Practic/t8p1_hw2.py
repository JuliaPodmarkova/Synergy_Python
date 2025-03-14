# Задача 2. Палиндром без цикла

def is_palindrome(my_list):
    def check_palindrome(start, end):
        if start >= end:
            return True
        if my_list[start] != my_list[end]:
            return False
        return check_palindrome(start + 1, end - 1)
    return check_palindrome(0, len(my_list) - 1)

print(is_palindrome([2, 3, 4, 3, 2]))
print(is_palindrome([2, 3,  3, 2]))
print(is_palindrome([2]))
print(is_palindrome([2, 3, 4, 3, 1]))
