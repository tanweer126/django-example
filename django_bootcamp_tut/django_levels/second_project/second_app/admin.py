from django.contrib import admin
from second_app.models import AccessRecord, Webpage, Topic, User1, UserProfileInfor

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User1)
admin.site.register(UserProfileInfor)
# Register your models here.
