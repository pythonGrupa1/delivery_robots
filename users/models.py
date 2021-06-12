#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy


#class User(AbstractUser):
    #class Types(models.TextChoices):
        #customer = 'Klient'
        #employee = 'Pracownik'

    #type = models.CharField(gettext_lazy('Type'), max_length=50, choices=Types.choices, default=Types.customer)

    #name = models.CharField(gettext_lazy('Name of user'), blank=True, max_length=255)

    #def get_absolute_url(self):
        #return reverse('users:detail', kwargs={'username': self.username})


#class Customer(User):
    #class Meta:
        #proxy = True


#class Employee(User):
    #class Meta:
        #proxy = True
