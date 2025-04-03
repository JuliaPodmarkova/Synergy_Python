#Задание 3. Преобразование времени
import datetime
time1 = 12873
time2 = 1200
time3 = 1234567

def time_to_time(n):
    h = n // 3600
    m = n % 3600 // 60
    s = n % 60
    print(str(h) + ':' + str(m) + ':' + str(s))

time_to_time(time1)
time_to_time(time2)
time_to_time(time3)


