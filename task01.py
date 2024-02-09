from pulp import LpMaximize, LpProblem, LpVariable

# Ініціалізуємо модель
model = LpProblem(name="maximize_production", sense=LpMaximize)

# Ініціалізуємо змінні рішення - кількість вироблених одиниць кожного напою
lemonade = LpVariable(name="Лимонад", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="Фруктовий сік", lowBound=0, cat='Integer')

# Об'єктивна функція - максимізація загальної кількості продуктів
model += (lemonade + fruit_juice), "Загальний обсяг виробництва"

# Додамо обмеження на використання ресурсів
# Лимонад: 2 од. води, 1 од. цукру, 1 од. лимонного соку
model += 2 * lemonade + fruit_juice <= 100, "Обмеження води"
model += lemonade <= 50, "Обмеження цукру"
model += lemonade <= 30, "Обмеження лімонного соку"
# Фруктовий сік: 2 од. фруктового пюре, 1 од. води
model += 2 * fruit_juice <= 40, "Обмеження фруктового пюре"

# Розв'язуємо модель
model.solve()

# Виведемо результат
print("Оптимальний план виробництва:")
print("Лимонад:", int(lemonade.varValue))
print("Фруктовий сік:", int(fruit_juice.varValue))
