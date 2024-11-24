#Задача 1
#my_str="120430"
#my_symbol="0"
#count = my_str.count(my_symbol)
#print(count)
#задача 2
my_str="3000"
my_symbol="0"
#
#count = 0
#while my_str.endswith(my_symbol):
    #count += 1
    #my_str = my_str[:-len(my_symbol)]

#print(count)
#задача 3
#my_list = [1, 2, 3, 4]
#new_list = my_list[1:] + [my_list[0]]
#print(new_list)
#задача 4
text = "43 більше за 34 , але меньше за 56"
words = text.split()  # Розділяємо рядок на окремі слова
total_sum = 0

# Проходимо по кожному елементу та перевіряємо, чи є це числом
for word in words:
    if word.isdigit():  # Перевіряємо, чи є це числом
        total_sum += int(word)  # Додаємо число до суми

print(total_sum)
