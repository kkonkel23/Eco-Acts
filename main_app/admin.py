from django.contrib import admin
from .models import Activity, MyActivity, Note

# Register your models here.
admin.site.register(Activity)
admin.site.register(MyActivity)
admin.site.register(Note)
