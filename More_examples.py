numbers = [1, 40, 300]
doubled_numbers = [n * 2 for n in numbers]
print(doubled_numbers) # [2,30,600]

string_numbers = ['42', '100', '6', '256']
int_numbers = [int(string) for string in string_numbers]
print(int_numbers) #[42,100,6,256]