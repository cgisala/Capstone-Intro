numbers = [1, -10, 40, -6, 500, 350]
positive_numbers = [n for n in numbers if n >= 0]
print(positive_numbers) #[1,40,350]

foods = ['cheese pizza', 'pepperoni pizza', 'ice cream', 'veggie pizza', 'tacos']
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas) #['cheese pizza', 'pepperoni pizza', 'veggie pizza']


#Using "in" operator
example = [1,5,10]
is_one_in_list = 1 in example # True
is_seven_in_list = 7 in example #False

print(f'Is one in list? {is_one_in_list}\n')
print(f'Is seven in list? {is_seven_in_list}\n')

course = 'ITEC 1150 Programming Logic'
if '1150' in course:
    print('This is Programming Logic')