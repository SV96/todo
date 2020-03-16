from django.db import models


# Create your models here.
class Tods(models.Model):
    Title = models.CharField(max_length=200)
    details = models.CharField(max_length=500)
    do_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.Title)

    class Meta:
        verbose_name_plural = 'Todss'
