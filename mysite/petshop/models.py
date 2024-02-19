from django.db import models
import datetime

dateNow=datetime.datetime.today()

# Create your models here.
class Animal(models.Model):
    #sempre pensar em alguma chave que identifique o objeto
    animalSpecie = models.CharField(max_length=10)
    animalName=models.CharField(max_length=15)
    animalBirth=models.DateField(null=True, blank=True)
    animalWidth=models.DecimalField(max_digits=4, decimal_places=2)
    animalHeigh=models.DecimalField(max_digits=4, decimal_places=2)
    
    # Função que retorna a idade do animal.
    '''@property
    def animalAge(self, animalBirth):

        animalBirth_str = self.animalBirth
        animalBirth_str_ = datetime.datetime.strptime(animalBirth_str, "%Y-%m-%d")
        animalAge=dateNow-self.animalBirth_

        if ((dateNow.month<=self.animalBirth_.month) and (dateNow.day<self.animalBirth_.day)):
            animalAge=(dateNow.year-self.animalBirth_.year)-1
        else:
            animalAge=dateNow.year-self.animalBirth_.year
        return animalAge'''
    
    def __str__(self):
        return f'Animal: {self.animalSpecie}'\
                f'Name: {self.animalName}'\
                f'Width: {self.animalWidth}'\
                f'Heigh: {self.animalHeigh}'\
                f'Birth: {self.animalBirth}'
    
class Customer(models.Model):
    customerId
    customerName