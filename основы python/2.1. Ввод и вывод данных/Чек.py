# Сдачу посчитать, конечно, все могут, но красивый чек напечатать — не так просто.

# Формат ввода
# - название товара;
# - цена товара;
# - вес товара;
# - количество денег у пользователя.

#Формат вывода
# - Чек
# - <название товара> - <вес>кг - <цена>руб/кг
# - Итого: <итоговая стоимость>руб
# - Внесено: <количество денег от пользователя>руб
# - Сдача: <сдача>руб


product_name = input()
product_price, product_weight = int(input()), int(input())
money = int(input())

print(f"Чек\n{product_name} - {product_weight}кг - {product_price}руб/кг")
print(f"Итого: {product_weight * product_price}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {money - product_weight * product_price}руб")
