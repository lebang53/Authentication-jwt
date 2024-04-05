from django.db import models
from enum import Enum as UserEnum, Enum
from django.contrib.auth.models import AbstractUser


class UserRoleEnum(UserEnum):
    ADMIN = 1
    LANDLORD = 2
    TENANT = 3


class User(AbstractUser):
    created_date = models.DateTimeField(auto_now_add=True)
    user_role = models.CharField(Enum(UserRoleEnum), default=UserRoleEnum.TENANT)
    avatar = models.ImageField(upload_to='avatars/')
    is_active = models.BooleanField(default=True)


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class House(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='houses_owned')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    room_count = models.PositiveIntegerField()
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='houses')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows')


class Image(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='images')
    url = models.URLField()

