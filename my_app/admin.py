from django.contrib import admin
from .models import Movie, Screening, Category, Review, Reservations, Feedback

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'cost', 'duration')
    list_filter = ('title', 'category')
    search_fields = ('title', 'category', 'age_limit')

class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'hall', 'total_seats')
    list_filter = ('date', 'time')
    search_fields = ('hall', 'time', 'total_seats')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'review_text')
    list_filter = ('name',)
    search_fields = ('name', 'review_text')

class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'age')
    list_filter = ('name', 'email')
    search_fields = ('name', 'phone_number', 'age')

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')
    list_filter = ('name', 'phone_number')
    search_fields = ('name', 'phone_number')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Screening, ScreeningAdmin)
admin.site.register(Category) 
admin.site.register(Review, ReviewAdmin)
admin.site.register(Reservations, ReservationsAdmin)
admin.site.register(Feedback, FeedbackAdmin)
