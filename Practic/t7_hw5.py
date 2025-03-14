# Задача 5. Сладкий бизнес

def profit(day, customers, course_usd):
    price_per_portion_usd = 2
    cost_per_portion_vatik = 30
    fine_weekend_vatik = 500

    # Вычисляем общую выручку в долларах
    total_revenue_usd = price_per_portion_usd * customers
    # Конвертируем выручку в ватик
    total_revenue_vatik = total_revenue_usd * course_usd

    # Вычисляем общие затраты
    total_cost_vatik = cost_per_portion_vatik * customers

    # Проверяем, является ли день выходным
    if day.lower() in ['saturday', 'sunday']:
        total_cost_vatik += fine_weekend_vatik

    # Вычисляем прибыль
    profit_vatik = total_revenue_vatik - total_cost_vatik
    return profit_vatik

print(profit('Wenesday', 13, 41))
print(profit('Saturday', 17, 70))
print(profit('Sunday', 1, 50))
