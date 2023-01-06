import datetime


def calculate_age(birth_date):
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


people = [{"name": 'Joe', "birthDate": datetime.datetime(1986, 10, 24)},
          {"name": 'Bob', "birthDate": datetime.datetime(1975, 5, 24)},
          {"name": 'Erika', "birthDate": datetime.datetime(1989, 6, 12)},
          {"name": 'Dylan', "birthDate": datetime.datetime(1999, 12, 14)},
          {"name": 'Steve', "birthDate": datetime.datetime(2003, 4, 24)}]

name_list = list(map(lambda person: 'Hello, my name is ' + person["name"] + 
                                    ' and I am ' + str(calculate_age(person['birthDate'])) + 
									' years old', people))
print(name_list)

