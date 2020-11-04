a = int(input("Введите количество километров, которые спортсмен пробежал в первый день: "))
e = a
b_one = int(input("Введите общее целевое расстояние за один день: "))
b_all = int(input("Введите общее целевое расстояние за все дни: "))
day_one = 1
day_all = 1
if a != b_one:
    while a < b_one:
        a = a + 0.1 * a
        day_one = day_one + 1
    while e < b_all:
        a = a + 0.1 * a
        day_all = day_all + 1
        e = e + a
print(f"Спорстмен достиг общего дневного расстояния на {day_one} день, общего расстояния - на {day_all} день")
