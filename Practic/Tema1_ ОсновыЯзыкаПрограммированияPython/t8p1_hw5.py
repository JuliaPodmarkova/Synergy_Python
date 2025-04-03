# Задача 5. Скобочные последовательности

def bracket_sequences(n):
    def generate(current, open_count, close_count):
        if open_count == close_count == n:
            sequences.append(current)
            return
        if open_count < n:
            generate(current + "(", open_count + 1, close_count)
        if close_count < open_count:
            generate(current + ")", open_count, close_count + 1)

    sequences = []
    generate("", 0, 0)
    return sequences

print(bracket_sequences(0))
print(bracket_sequences(1))
print(bracket_sequences(2))
