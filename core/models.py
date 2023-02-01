from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50,blank=False)
    description = models.TextField(blank=True)
    important = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        # return f'[{self.pk}]{self.title}'
        return self.title