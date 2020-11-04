a = int(input("Введите количество секунд, которые вам понадобятся для обезвреживания конфетной бомбы:"))
hours = a // 3600
if hours < 10:
    hours = f"0{hours}"
minutes = (a % 3600) // 60
if minutes < 10:
    minutes = f"0{minutes}"
seconds = (a % 3600) % 60
if seconds < 10:
    seconds = f"0{seconds}"
print(f"Если конфетные бобмы существуют, на вашем таймере будет обозначено время: {hours}:{minutes}:{seconds}")
