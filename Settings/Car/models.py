from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.serializer_fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    STATUS_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer')
    )
    username = models.CharField(max_length=16, unique=True)
    phone_number = PhoneNumberField(unique=True, region=None)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    data_registered = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.username

class Car(models.Model):
    MARK_CHOICES = (
        ('toyota', 'Toyota'),
        ('lexus', 'Lexus'),
        ('honda', 'Honda'),
        ('volvo', 'Volvo'),
        ('chevrolet', 'Chevrolet'),
        ('ford', 'Ford'),
        ('mazda', 'Mazda'),
        ('mercedes-benz', 'Mercedes-Benz'),
        ('volkswagen', 'Volkswagen'),
        ('hyundai', 'Hyundai'),
        ('nissan', 'Nissan'),
        ('audi', 'Audi'),
        ('mitsubishi', 'Mitsubishi'),
        ('bmw', 'Bmw')
    )

    mark = models.CharField(choices=MARK_CHOICES)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    region = CountryField()
    price = models.PositiveSmallIntegerField()
    year = models.PositiveSmallIntegerField()
    model = models.CharField(max_length=64)
    condition = models.CharField(max_length=64)
    cylinders = models.CharField(max_length=64)
    fuel = models.CharField(max_length=64)
    odometer = models.CharField(max_length=64)
    title_status = models.CharField(max_length=64)
    transmission = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    paint_color = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    posting_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.mark} - {self.price}'

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    comment = models.TextField()
    created_date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.user} - {self.rate}/10'