from django.db import models


class Class(models.Model):
    CLASS = (
        ('I', 'I'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('V', 'V'),
        ('VI', 'VI'),
        ('VII', 'VII'),
        ('VIII', 'VIII'),
        ('IX', 'IX'),
        ('X', 'X'),
        ('XI', 'XI'),
        ('XII', 'XII'),
    )
    std = models.CharField(max_length=20, choices=CLASS)

    # def get_modules(self):
    #     modules = Module.objects.filter(subject=self)
    #     return modules

    def __str__(self):
        return self.std


class Subject(models.Model):
    title = models.CharField(max_length=200)
    std = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='subject')

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.TextField(max_length=1000)

    def __str__(self):
        return self.topic.title+':'+self.question[:15]


class Choice(models.Model):
    ANSWER = (
        ('a', 'a'),
        ('b', 'b'),
        ('c', 'c'),
        ('d', 'd'),
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.CharField(max_length=50)
    d = models.CharField(max_length=50)
    answer = models.CharField(max_length=1, choices=ANSWER)

    def __str__(self):
        return self.question


class Score(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    obtained = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.question
