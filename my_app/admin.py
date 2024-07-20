from django.contrib import admin
from .models import *

admin.site.register([Movie,Screening,Category,Review,Reservations,Feedback])