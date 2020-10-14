from django.contrib import admin
from .models import Activity, MyActivity, Note, BlogPost

# Register your models here.
admin.site.register(Activity)
admin.site.register(MyActivity)
admin.site.register(Note)
admin.site.register(BlogPost)
