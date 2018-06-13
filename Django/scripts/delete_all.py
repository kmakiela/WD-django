from WD.models import *


def run():
    students = Student.objects.all()
    students.delete()

    cs = Course.objects.all()
    cs.delete()

    ms = Mark.objects.all()
    ms.delete()

    ps = ParticipantList.objects.all()
    ps.delete()