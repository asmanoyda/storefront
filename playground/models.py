from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    mobile_no = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username


class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Cold_drinks(models.Model):
    name = models.CharField(max_length=255, default="none")
    
    brand = models.CharField(max_length=255, default="none")
    flavor = models.CharField(max_length=255, default="none")

class Peoples(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(max_length=255)


class Cars(models.Model):
    model = models.CharField(max_length=255, default="none")
    year = models.IntegerField(max_length=255, default="none")
    color = models.CharField(max_length=255, default="none")


class Stocks(models.Model):
    name = models.CharField(max_length=255, default="none")
    price = models.IntegerField(max_length=255, default="none")
    sector = models.CharField(max_length=255, default="none")


class Chocos(models.Model):
    brand = models.CharField(max_length=255, default="none")
    type = models.CharField(max_length=255, default="none")
    cocoa_percentage = models.IntegerField(max_length=255, default="none")
    price = models.IntegerField(max_length=255, default="none")
    sugar_percentage = models.IntegerField(max_length=255, default="none")


class Students(models.Model):
    name = models.CharField(max_length=255, default="none")
    age = models.IntegerField(max_length=255, default="none")
    major = models.CharField(max_length=255, default="none")
    grades = models.IntegerField(max_length=255, default="none")

class Companys(models.Model):
    name = models.CharField(max_length=255, default="none")
    sector = models.CharField(max_length=255, default="none")
    location = models.CharField(max_length=255, default="none")


class Teachers(models.Model):
    name = models.CharField(max_length=255, default="none")
    subject = models.CharField(max_length=255, default="none")
 


