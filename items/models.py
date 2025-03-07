from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class LostItem(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField()
    location = models.CharField(max_length=255)
    date_lost = models.CharField(max_length=255)
    image = models.ImageField(upload_to="lost_items/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    is_found = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class FoundItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_found = models.CharField(max_length=255)
    image = models.ImageField(upload_to="found_items/", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2)
    is_claimed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User

class ClaimRequest(models.Model):
    lost_item = models.ForeignKey("LostItem", on_delete=models.CASCADE, blank=True, null=True)  # Если человек нашёл потерянный предмет
    found_item = models.ForeignKey("FoundItem", on_delete=models.CASCADE, blank=True, null=True)  # Если человек хочет забрать предмет
    name = models.CharField(max_length=255)  # Имя того, кто оставляет заявку
    phone_number = models.CharField(max_length=20)  # Номер телефона
    message = models.TextField(blank=True, null=True)  # Дополнительное сообщение
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  # Админ может подтвердить

    def __str__(self):
        return f"Заявка на {self.lost_item or self.found_item} от {self.name}"
