# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

print(sum(list(map(lambda x: 0 if x == '.' else int(x), input('введите вещественное число: ')))))