from django.db import models
import uuid
# Create your models here.
class Book(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=50)
    number_of_pages = models.IntegerField()
    published_date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self) :
        return self.title

        