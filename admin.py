from django.contrib import admin

from .models import AyurvedicOptions
from .models import AyurvedicQuestion
from .models import UserResponse

# Register your models here.
admin.site.register(AyurvedicOptions)
admin.site.register(AyurvedicQuestion)
admin.site.register(UserResponse)
