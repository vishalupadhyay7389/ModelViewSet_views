from django.db import models
from rest_framework import serializers
from django.core.validators import MinLengthValidator , RegexValidator

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    roll_number = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=15 , validators=[MinLengthValidator(10,message='mobile number must be at least 10 digit long'),RegexValidator(r'^9\d{9}$' , message = 'mobile number must be start with 9 and be digit long.')] )
    image = models.ImageField(upload_to='Images')
    address = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

class StudentSerlizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'