from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import *


ROLES_CHOICES = (
	("ADMIN", "admin"),
	("SUPERMANAGER", "supermanager"),
	("MANAGER", "manager"),
	('DILER', 'diler'),
	("CLIENT", "client"),
)


# Create your models here.
class CustomUser(AbstractBaseUser):
	username = models.CharField(verbose_name='Имя пользователя', max_length=150, null=False, default=None, unique=True)
	email = models.EmailField(unique=True, null=True, default=None, blank=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	name = models.CharField(verbose_name='Имя', max_length=150, null=True, default=None, blank=True)
	surname = models.CharField(verbose_name='Фамилия', max_length=150, null=True, default=None, blank=True)
	clear_password = models.CharField(max_length=255, null=True, default=None)

	role = models.CharField(verbose_name='Роль', max_length=150, null=True, default='CLIENT', choices=ROLES_CHOICES)
	sub_role = models.CharField(verbose_name='', max_length=100, null=True, default=None)
	dealer_name = models.CharField(verbose_name='', max_length=255, null=True, default=None)

	objects = CustomUserManager()
	USERNAME_FIELD = 'username'

	def set_password(self, password):
		self.clear_password = password
		super().set_password(password)

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser

	def get_privs(self):
		return []

	def get_name(self):
		return f'{self.name} {self.surname}'

	class Meta:
		db_table = 'auth_user'
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'

	def __str__(self):
		return f'{self.name} {self.surname}'


class Document(models.Model):
	title = models.CharField(verbose_name='Название', max_length=150, default=None)
	document = models.FileField(upload_to='documents', verbose_name='Файл')
	owner = models.CharField(verbose_name='Владелец', max_length=150, null=True, default=None, blank=True)
	last_modified = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Документ'
		verbose_name_plural = 'Документы'


class Activity(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
	action = models.CharField(verbose_name='Действие', max_length=150)
	ip = models.CharField(verbose_name='IP', max_length=150, default=None, null=True, blank=True)
	time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Активность'
		verbose_name_plural = 'Активности'
