a = 2
print(type(a))
b = 2.0
print(type(b))
c = "2.0"
print(type(c))
name = input("Wprowadz swoje imie ")
print(f"Czesc, {name}!")

age = int(input("ile masz lat? "))
birth_year = 2019 - age
print(f'Urodziles sie w {birth_year} roku')
v = int(input("Wprowadz liczbe od 1 do 10: "))
print(v + 10)
name = input("Wprowadz swoje imie: ")
print(f'Czesc, {name}! Jak sie masz?')
a = float("1")
b = int(2.5)
c = bool(1)
d = bool('')
e = bool(0)
print(a)
print(b)
print(c)
print(d)
print(e)
name = "Ika"    
b = "Czesc, " 
print(b + name)

a = "Stoi na stacji lokomotywa, ciezka, ogromna i pot z nije splywa"
print(len(a.split()))
b = "stoi.na.stacji.lokomotywa"
print(b.split('.'))

first_name = "Karo "
second_name = "Gorska"
print(f'{first_name} {second_name}')

number = [3 , 5 , 7 , 9 , 10.5]
print(number)
number.append("Python")
print(number)
print(len(number))
print(number)
print(number[5])
print(number[2:5])
del number[5]
print(number)
print(5 in number)
print(number.index(9))

names = ["Tom" , "Bim" , "Kas" , "Wit"]
print(names)
print(names[0])
names.append("Dim")
print(names)
names.remove("Dim")
print(names)