from django.contrib import admin
from .models import Aboutus, CourseOffered, Gallery, PremiumCourse, StudentRegister, PremiumCourseEnroll,relatedCourses

# Register your models here.
admin.site.register(Aboutus)
admin.site.register(CourseOffered)
admin.site.register(Gallery)
admin.site.register(PremiumCourse)
admin.site.register(StudentRegister)
admin.site.register(PremiumCourseEnroll)
admin.site.register(relatedCourses)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'



