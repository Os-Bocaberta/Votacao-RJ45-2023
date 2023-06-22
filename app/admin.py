from django.contrib import admin
from .models import Candidates, Voters

# Register your models here.

admin.site.register(Candidates)
admin.site.register(Voters)
