from django.db import models


# Create your models here.

class Aboutus(models.Model):
    about_id = models.AutoField
    about_category = models.CharField(max_length=50, default="")
    about_desc = models.TextField()
    about_image = models.ImageField(upload_to="images/about", default="")

    def __str__(self):
        return self.about_category


class CourseOffered(models.Model):
    course_id = models.AutoField
    course_title = models.CharField(max_length=50, default="")
    course_category = models.CharField(max_length=50, default="")
    course_desc = models.TextField()
    course_chapter = models.TextField()
    course_duration = models.CharField(max_length=50, default="")
    course_image = models.ImageField(upload_to="images/courses", default="")

    def __str__(self):
        return self.course_title


Gallery_CHOICES = (
    ('all', 'ALL'),
    ('lab', 'LAB'),
    ('classroom', 'CLASSROOM'),
    ('students', 'STUDENTS'),
    ('other', 'OTHER'),
)


class Gallery(models.Model):
    gallery_id = models.AutoField
    gallery_title = models.CharField(max_length=50, default="")
    gallery_cat = models.CharField(max_length=20, choices=Gallery_CHOICES, default='all')
    gallery_image = models.ImageField(upload_to="images/gallery", default="")

    def __str__(self):
        return self.gallery_title


class PremiumCourse(models.Model):
    course_id = models.AutoField
    course_title = models.CharField(max_length=50, default="")
    course_desc = models.TextField()
    course_icon = models.ImageField(upload_to="images/premiumcoursesicon", default="")

    def __str__(self):
        return self.course_title


class StudentRegister(models.Model):
    std_id = models.AutoField
    first_name = models.CharField(max_length=50, default="")
    middle_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    birthdate = models.DateField()
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    email = models.EmailField()
    mobile = models.CharField(max_length=50, default="")
    course = models.ForeignKey(CourseOffered, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name


GENDER = (
    ('select', 'SELECT'),
    ('Male', 'MALE'),
    ('Female', 'FEMALE'),
    ('Other', 'OTHER'),
)


class PremiumCourseEnroll(models.Model):
    crsenroll_id = models.AutoField
    name = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=20, choices=GENDER, default="Select")
    city = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    email = models.EmailField()
    premium_course = models.ForeignKey(PremiumCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class relatedCourses(models.Model):
    rc_id = models.AutoField(primary_key=True)
    rc_name = models.CharField(max_length=50, default="")
    rc_description = models.CharField(max_length=140, default="")
    rc_category = models.CharField(max_length=50, default="")
    rc_duration = models.CharField(max_length=50, default="")
    rc_image = models.ImageField(upload_to="images/relatesdcourses", default="")

    def __str__(self):
        return self.rc_name
