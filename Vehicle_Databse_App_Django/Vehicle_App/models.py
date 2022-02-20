from distutils.command.upload import upload
from django.db import models
from model_utils import Choices



class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=200)
    vehicle_model = models.CharField(max_length=200)
    speed = models.IntegerField()
    avg_speed = models.IntegerField()
    tempreture = models.IntegerField()

    FUEL_CHOICES = Choices(
       'Tank Full',
       'Tank Half',
       'Empty',
   )
    
    fuel = models.CharField(
        max_length=32,
        choices=FUEL_CHOICES,
    )

    ENG_STATUS = Choices(
       'Good',
       'Bad',
   )

    engine = models.CharField(
        max_length=32,
        choices=ENG_STATUS,
    )

    ENG_POWER = Choices(
        'ON',
        'OFF',
       
   )

    power = models.CharField(
       max_length=32,
       choices=ENG_POWER,
   )
    static_map = models.ImageField(upload_to = 'Vehicle_App/static/Images')
    camera_one = models.CharField(
        max_length=32,
        choices=Choices(
            "Camera 1",
        )
    )
    camera_two = models.CharField(
        max_length=32,
        choices=Choices(
            "Camera 2",
        )
    )
    def __str__(self):
        return self.vehicle_number




    




# Create your models here.

