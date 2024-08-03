from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

payments = (
    ("Online", "Online"),    
    ("Cash", "Cash"),
    ("by bank card", "by bank card"),                  
)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    duration = models.CharField(max_length=30)
    age_limit = models.IntegerField()
    release_date = models.DateField()  
    cost = models.IntegerField()
    description = models.TextField()
    director = models.CharField(max_length=100)
    starring = models.CharField(max_length=255)
    image = models.ImageField(upload_to='movies/images/', blank=True, null=True)
    video = models.FileField(upload_to='movies/videos/', blank=True, null=True)

    def __str__(self):
        return self.title

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    hall = models.CharField(max_length=100)
    total_seats = models.IntegerField() 

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time} - {self.hall}"

    def booked_seats_count(self):
        return Reservations.objects.filter(screening=self).count()

    def available_seats(self):
        return self.total_seats - self.booked_seats_count()

class Review(models.Model):
    name = models.CharField(max_length=50)
    review_text = models.TextField()

    def __str__(self) -> str:
        return self.name

class Reservations(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15) 
    age = models.IntegerField()
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)  
    payment = models.CharField(choices=payments, max_length=20)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    @property
    def amount_to_be_paid(self):
        return self.screening.movie.cost

    def clean(self):
        if Reservations.objects.filter(screening=self.screening, seat_number=self.seat_number).exists():
            raise ValidationError(f'The seat {self.seat_number} for the movie {self.screening.movie.title} on {self.screening.date} at {self.screening.time} is already taken.')

        if self.screening.available_seats() <= 0:
            raise ValidationError(f'No available seats for the movie {self.screening.movie.title} on {self.screening.date} at {self.screening.time}.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    text_of_the_appeal = models.TextField()

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Reservations)
def set_session_date(sender, instance, **kwargs):
    if instance.screening:
        instance.session_date = instance.screening.date

