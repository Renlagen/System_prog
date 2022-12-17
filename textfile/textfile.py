Country = str(input('Введите страну:'))
City = str(input('Введите город:'))
Street = str(input('Введите улицу:'))
House = str(input('Введите дом:'))

List = [Country, City, Street, House]

with open('listfile.txt', 'w') as filehandle: filehandle.writelines("%s\n" % place for place in List)
places = []
with open('listfile.txt', 'r') as filehandle: filecontents = filehandle.readlines()

for line in filecontents:
    current_place = line[:-1]
    places.append(current_place)
