from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, studentNo, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            studentNo=studentNo
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, studentNo, password):
        user = self.create_user(
            email,
            password=password,
            name = name,
            studentNo = studentNo
        )
        # user.is_superuser = True
        user.is_admin = True
        # user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=30, null=False, unique=True)
    name = models.CharField(max_length=15, null=False)
    studentNo = models.CharField(max_length=8, null=False)
    is_admin = models.BooleanField(default=False)
    vote = models.OneToOneField('mainapp.Post', null=True, on_delete=models.CASCADE, related_name='vote')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'studentNo']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
       return self.is_admin


