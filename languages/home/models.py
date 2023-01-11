from django.db import models
from django.contrib.auth.models import User
class Students(models.Model):
    roll=models.CharField(max_length=20)
    name=models.CharField(max_length=50)
    dob=models.DateField(auto_now=False)
    ch=(
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    gen=models.CharField(max_length=11,choices=ch)
    fees=models.IntegerField()
    about=models.TextField()
    img=models.ImageField(upload_to='pics')
    def __str__(self) -> str:
        return self.name
class Language(models.Model):
    lname=models.CharField(max_length=20)
    fees=models.IntegerField()
    duration=models.CharField(max_length=15)
    trainer=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.lname+" "+self.trainer

# REGISTERED_USER_FROM_USERSIDE
class Emp(User):    
    mob=models.CharField(max_length=11)
    address=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.address

# START_ONE_TO_MANY_RELATIONSHIP

class Trainer(models.Model):
    name=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    languages=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
class Student(models.Model):
    sname=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.sname

#  END_ONE_TO_MANY_RELATIONSHIP

#  START_MANY_TO_MANY_FIELD_RELATIONSHIP

class Vendor(models.Model):
    vname=models.CharField(max_length=20)
    vaddress=models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.vname+" "+self.vaddress
class Customer(models.Model):                                           
    cname=models.CharField(max_length=20)
    caddress=models.CharField(max_length=40)
    vendors=models.ManyToManyField(Vendor)
    def __str__(self) -> str:
        return self.cname+" "+self.caddress

# END_MANY_TO_MANY_FIELD_RELATIONSHIP

# START_ONE_TO_ONE_FIELD_RELATIONSHIP

class Ceo(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Address(models.Model):
    ceo=models.OneToOneField(Ceo,on_delete=models.CASCADE,primary_key=True)
    street=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=10)
    def __str__(self):
        return self.street+" "+self.city

# END_ONE_TO_ONE_FIELD_RELATIONSHIP

