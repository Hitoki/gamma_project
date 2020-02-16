from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    is_superuser = models.BooleanField()
    e_mail = models.EmailField()


class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    hire_date = models.DateField('hire date')
    dismiss_date = models.DateField('dismissing date', blank=True, null=True)


class Schedule(models.Model):
    shop = models.ForeignKey('Shops', on_delete=models.CASCADE,)
    staff_member = models.ForeignKey('Staff', on_delete=models.CASCADE,)
    date = models.DateField('working day')
    hours = models.PositiveIntegerField()


class Shops(models.Model):
    name = models.CharField(max_length=20)


class Costs(models.Model):
    name = models.CharField(max_length=20)


class ActivityLog(models.Model):
    date = models.DateField('day')
    shop = models.ForeignKey('Shops', on_delete=models.CASCADE,)
    cost = models.ForeignKey('Costs', on_delete=models.CASCADE,)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    staff_member = models.ForeignKey('Staff', on_delete=models.CASCADE,)
    comment = models.CharField(max_length=50)
