from django.shortcuts import render
from .models import Student, Course, Mark, ParticipantList
# Create your views here.


def show_student_info(request, name):
    student = Student.objects.get(name=name)
    clist = ParticipantList.objects.filter(student=student)
    context = {
        's': student,
        'clist': clist,
    }
    return render(request, 'WD/student.html', context)


def show_all_courses(request):
    cs = Course.objects.all()
    context = {
        'cs': cs,
    }
    return render(request, 'WD/courses.html', context)


def show_course_info(request, topic):
    course = Course.objects.get(topic=topic)
    plist = ParticipantList.objects.filter(course=course)
    context = {
        'plist': plist,
        'course': course
    }
    return render(request, 'WD/course.html', context)


def show_all_students(request):
    ss = Student.objects.all()
    context = {
        'ss': ss,
    }
    return render(request, 'WD/students.html', context)


def main_view_wd(request):
    context = {}
    return render(request, 'WD/WD.html', context)
