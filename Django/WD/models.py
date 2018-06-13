from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name


class Course(models.Model):
    topic = models.CharField(max_length=100)
    max_participants = models.IntegerField(default=0)
    participants = models.ManyToManyField(Student, through='ParticipantList', through_fields=('course', 'student'))

    def __str__(self):
        return self.topic


class Mark(models.Model):
    value = models.PositiveSmallIntegerField(default=1)
    comment = models.TextField(max_length=300, null=True)
    first_try = models.BooleanField(default=True)

    def __str__(self):
        return str(self.value)


class ParticipantList(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s is enrolled in %s with mark:%s" % (self.student, self.course, self.mark)
