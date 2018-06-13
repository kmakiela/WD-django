from WD.models import *
import datetime


def run():
    c1 = Course(topic='Python', max_participants=10); c1.save()
    c2 = Course(topic='Julia', max_participants=5); c2.save()
    c3 = Course(topic='Operating Systems', max_participants=3); c3.save()
    c4 = Course(topic='Erlang', max_participants=2); c4.save()

    s1 = Student(name='Ala', birthdate=datetime.date(1997, 1, 1)); s1.save()
    s2 = Student(name='Bob', birthdate=datetime.date(1997, 12, 11)); s2.save()
    s3 = Student(name='Cyprian', birthdate=datetime.date(1998, 3, 4)); s3.save()
    s4 = Student(name='Dawid', birthdate=datetime.date(1996, 3, 9)); s4.save()
    s5 = Student(name='Eleonora', birthdate=datetime.date(1998, 6, 6)); s5.save()
    s6 = Student(name='Filip', birthdate=datetime.date(1997, 7, 13)); s6.save()
    s7 = Student(name='Gustaw', birthdate=datetime.date(1998, 2, 6)); s7.save()
    s8 = Student(name='Helena', birthdate=datetime.date(1996, 12, 30)); s8.save()

    m1 = Mark.objects.create(value=2, first_try=True)
    m2 = Mark.objects.create(value=3, first_try=True)
    m3 = Mark.objects.create(value=4, first_try=True)
    m4 = Mark.objects.create(value=5, first_try=True)

    ParticipantList.objects.create(course=c1, student=s1, mark=m1)
    ParticipantList.objects.create(course=c1, student=s2)
    ParticipantList.objects.create(course=c1, student=s3)
    ParticipantList.objects.create(course=c1, student=s4, mark=m2)

    ParticipantList.objects.create(course=c2, student=s5, mark=m3)
    ParticipantList.objects.create(course=c2, student=s6, mark=m1)
    ParticipantList.objects.create(course=c2, student=s7, mark=m4)

    ParticipantList.objects.create(course=c3, student=s1, mark=m1)
    ParticipantList.objects.create(course=c3, student=s2)
    ParticipantList.objects.create(course=c3, student=s3, mark=m3)
    ParticipantList.objects.create(course=c3, student=s4)
    ParticipantList.objects.create(course=c3, student=s8, mark=m4)


