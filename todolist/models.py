from django.db import models
from django.db import models
from users.models import Users
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="todolist") 
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="todo_images/", null=True, blank=True)

    def __str__(self):
        return self.title