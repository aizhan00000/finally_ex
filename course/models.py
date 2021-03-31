from django.db import models
# from .models import Course


class Course(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Languages(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Details(models.Model):
    title = models.CharField(max_length=100)
    pr_languages = models.ForeignKey(Languages, on_delete=models.SET_NULL, null=True)
    price_per_month = models.IntegerField()
    duration = models.CharField(max_length=100)

    def __str__(self):
        return str(self.pr_languages) + str(self.title)


class Enrollment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pr_language = models.CharField(max_length=69)
    title = models.CharField(max_length=50)

    class Meta:
        def __str__(self):
            return 'enrollment {}'.format(self.id)
