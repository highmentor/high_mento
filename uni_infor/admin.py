from django.contrib import admin
from .models import University, University_review#, University_major_data
# Register your models here.
admin.site.register(University)
admin.site.register(University_review)
# admin.site.register(University_major_data)