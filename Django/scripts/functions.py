from WD.models import *
import datetime


def run():
    get_students_who_passed(Course.objects.get(topic='Julia'))
    get_students_who_did_not_pass(Course.objects.get(topic='Julia'))
    get_students_born_before(datetime.date(1997, 12, 12))
    get_students_born_after(datetime.date(1997, 12, 12))


def get_students_who_passed(course):
    s = "Students who passed %s:" % course.topic
    plist = ParticipantList.objects.filter(course=course)
    for p in plist:
        if p.mark is not None and p.mark.value>2:
            s = "%s %s with %s," % (s, p.student.name,str(p.mark.value))
    print(s)


def get_students_who_did_not_pass(course):
    s = "Students who did not pass %s:" % course.topic
    plist = ParticipantList.objects.filter(course=course)
    for p in plist:
        if p.mark is not None and p.mark.value == 2:
            s = "%s %s," % (s, p.student.name)
    print(s)


def get_students_born_before(date):
    ret = "Students born before %s:\n" % str(date)
    for s in Student.objects.all():
        if s.birthdate < date:
            ret = "%s %s born %s\n" % (ret, s.name, s.birthdate)
    print(ret)


def get_students_born_after(date):
    ret = "Students born after %s:\n" % str(date)
    for s in Student.objects.all():
        if s.birthdate > date:
            ret = "%s %s born %s\n" % (ret, s.name, s.birthdate)
    print(ret)


