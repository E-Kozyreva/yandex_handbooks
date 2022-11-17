# Чаще всего автоматизация идёт на пользу.
# Одна из задач, в которой лучше исключить человеческий фактор, — подсчёт сдачи.
# Определите, какую сдачу нужно выдать тому, кто купил 2,5кг черешни по цене 38 руб/кг.

# Формат ввода
# Одно натуральное число - номинал купюры пользователя (\ge 100≥100).

# Формат вывода
# Одно натуральное число — размер сдачи.

money, price = int(input()), int(2.5 * 38)
print(money - price)
