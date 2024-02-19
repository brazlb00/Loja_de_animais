from Animal import Animal
import datetime

dateNow=datetime.datetime.today()
animalBirth_str = "2019-02-09"
animalBirth = datetime.datetime.strptime(animalBirth_str, "%Y-%m-%d")
animalAg_date=dateNow-animalBirth

if ((dateNow.month<=animalBirth.month) and (dateNow.day<animalBirth.day)):
    animalAg_date=(dateNow.year-animalBirth.year)-1
else:
    print('cai aqui')
    animalAg_date=dateNow.year-animalBirth.year
print('Mes: ', animalBirth.month)
print('Dia: ', animalBirth.day)
print('Idade: ', animalAg_date)