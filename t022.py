# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

my_list = [12, 'sa,df', 5643]
# x1 = list(filter(lambda i:  str(i).isalpha my_list))     #  isalpha  состоит ли строка из букв?
x1 = list(filter(lambda i: isinstance(i, str), my_list))   #  isinstance i это строка?   
x2 = list(filter(lambda i: str(i).isdigit(), my_list))     #  isdigit состоит ли строка из цифр?
# x2 = list(filter(lambda i: isinstance(i, (int,float)), my_list))
print(x1, ',', x2)
