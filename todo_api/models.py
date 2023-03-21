import uuid
from django.db import models


class TBL_TODO(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField(max_length=255, unique=True)
    description= models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "todo"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.task


# Test one to one relationship between author model and book model then migrate
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_author"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.name

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tbl_book"
        ordering = ['-createdAt']

        def __str__(self) -> str:
            return self.title

