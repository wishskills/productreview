from django.contrib import admin
from .models import Laptop, Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('laptop', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Laptop)
admin.site.register(Review, ReviewAdmin)
