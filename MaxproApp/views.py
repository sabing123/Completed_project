from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm, PremiumCourseForm
from .models import Aboutus, CourseOffered, Gallery, PremiumCourse, StudentRegister, PremiumCourseEnroll,relatedCourses
import random
from random import choice

def index(request):
    permiumCourses = PremiumCourse.objects.all()
    print(permiumCourses)
    return render(request, 'index.html', {'permiumCourses': permiumCourses})


def gallery(request):
    labgallery = Gallery.objects.filter(gallery_cat='lab')
    classroomgallery = Gallery.objects.filter(gallery_cat='classroom')
    Studentgallery = Gallery.objects.filter(gallery_cat='students')
    othersgallery = Gallery.objects.filter(gallery_cat='other')
    params = {'labgallery': labgallery, 'classroomgallery': classroomgallery, 'Studentgallery': Studentgallery,
              'othersgallery': othersgallery}
    return render(request, 'gallery.html', params)


def courseDetails(request, myid):

    courseinfo = CourseOffered.objects.filter(id=myid)
    print(courseinfo)
    RelatedCourses = relatedCourses.objects.all()
    # random_list = random.sample(RelatedCourses, 3)
    # MyRandomChoice = choice(relatedCourses.objects.all())
    # random_list = random.choice(RelatedCourses)

    print(RelatedCourses)

    return render(request, 'course-detail.html',
                  {'courseinfo': courseinfo[0],
                   'relatedCourses':RelatedCourses})


def courseEnroll(request, myid,):
    courseinfo = CourseOffered.objects.filter(id=myid)
    print(courseinfo)
    return render(request, 'enroll.html', {'courseinfo': courseinfo[0]})


def course(request):
    courses = CourseOffered.objects.all()
    course_paginator = Paginator(courses, 1)
    page_num = request.GET.get('page')
    page = course_paginator.get_page(page_num)
    params = {'page': page}
    return render(request, 'course.html', params)


def aboutus(request):
    ab1 = Aboutus.objects.filter(about_category='MaxPro Computer')
    ab2 = Aboutus.objects.filter(about_category='About Us')
    ab3 = Aboutus.objects.filter(about_category='About Classes')
    params = {'ab1': ab1, 'ab2': ab2, 'ab3': ab3}
    return render(request, 'about.html', params)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            comment = name + " with the email, " + email + " sent the following message:\n\n" + message;
            send_mail(name, comment, 'maxpro.institute@gmail.com', ['maxpro.institute@gmail.com'])
            # context= {'form': form}
            # return render(request, 'contact.html', context)
            messages.success(request, 'Thank You! Your messages has been submitted successfully.')
            return HttpResponseRedirect('/contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        course = CourseOffered.objects.none()
    else:
        coursetitle = CourseOffered.objects.filter(course_title__icontains=query)
        coursecategories = CourseOffered.objects.filter(course_category__icontains=query)
        course = coursetitle.union(coursecategories)
        page = request.GET.get('page', 1)
        paginator = Paginator(course, 2)
        try:
            course = paginator.page(page)
        except PageNotAnInteger:
            course = paginator.page(1)
        except EmptyPage:
            course = paginator.page(paginator.num_pages)
    params = {'course': course, 'query': query}
    return render(request, 'search.html', params)


def studentReg(request, myid):
    courseinfo = CourseOffered.objects.get(id=myid)
    if request.method == "POST":
        first_name = request.POST['q4_studentName[first]']
        middle_name = request.POST['q4_studentName[middle]']
        last_name = request.POST['q4_studentName[last]']
        month = request.POST['q24_birthDate24[month]']
        day = request.POST['q24_birthDate24[day]']
        year = request.POST['q24_birthDate24[year]']
        gender = request.POST['q3_gender']
        city = request.POST['q23_address[city]']
        state = request.POST['q23_address[state]']
        email = request.POST['q6_studentEmail6']
        mobile = request.POST['q27_mobileNumber[full]']
        birthdate = year + '-' + month + '-' + day
        studentReg = StudentRegister.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                                                    birthdate=birthdate, gender=gender, city=city, state=state,
                                                    email=email, mobile=mobile, course=courseinfo)
        studentReg.save()
        messages.success(request, 'Thank You! You have form has been submitted successfully. Please check your mail.')
        # Message for user registering the form
        name = first_name + ' ' + middle_name + ' ' + last_name
        comment = "You have successfully submitted the form to enroll in the " + str(courseinfo) + " course in our institute. You will soon here from us."
        send_mail(name, comment, 'maxpro.institute@gmail.com', [email])

        # Message for admin
        message = "User with the name " + name + " has enrolled in the " + str(courseinfo) + " course through the website, his email is " + email + " and Mobile No. is " + mobile;
        send_mail('Admin', message, 'maxpro.institute@gmail.com', ['maxpro.institute@gmail.com'])
        return HttpResponseRedirect('/enroll/'+ str(myid))
    return render(request, 'enroll.html', {'courseinfo': courseinfo})


def terms(request):
    return render(request, 'termsAndConditions.html')


# def premiumenroll(request):
#     form= PremiumCourseForm()
#     return render(request, 'premiumform.html',{'form':form})

def premiumreg(request):
    if request.method == 'POST':
        form = PremiumCourseForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            gender = form.cleaned_data.get('gender')
            city = form.cleaned_data.get('city')
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            pcourse = form.cleaned_data.get('premium_course')
            penroll = PremiumCourseEnroll.objects.create(name=name, gender=gender, city=city, phone=phone, email=email,
                                                         premium_course=pcourse)
            penroll.save()
            messages.success(request,
                             'Thank You! You have form for Premium course has been submitted successfully. Please check your mail.')
            # Message for user registering the form
            comment = " You have successfully submitted the form to enroll in the premium course in our institute. You will soon here from us."
            send_mail(name, comment, 'maxpro.institute@gmail.com', [email])

            # Message for admin
            message = "Student with the name " + name + " has enrolled in the " + str(pcourse) + " course through the website, his email is " + email + " and Mobile No. is " + phone;
            send_mail('Admin', message, 'maxpro.institute@gmail.com', ['maxpro.institute@gmail.com'])
            return HttpResponseRedirect('/premiumcourse')
    else:
        form = PremiumCourseForm()
    return render(request, 'premiumform.html', {'form': form})
