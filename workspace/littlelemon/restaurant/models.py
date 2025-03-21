from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    BookingDate = models.DateTimeField()


class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
