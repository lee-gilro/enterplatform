from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin

# 헬퍼 클래스
class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        superuser = self.create_user(
            email=email,
            password=password,
        )

        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save(using=self._db)
        return superuser
    

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male","Male")
        FEMALE = ("female","Female")
    class LanguageChoices(models.TextChoices):
        KR = ("kr","Korean")
        EN = ("en", "English")
    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"
    nickname = models.CharField(max_length=150, default="",)
    is_artist = models.BooleanField(default=False)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    avatar = models.URLField(blank=True) # default 로 회색 화면 설정필요
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,null=True, blank=True,)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices,null=True, blank=True,)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices,null=True, blank=True,)
    country = models.CharField(max_length=50, default="KOR")
    address = models.CharField(max_length=200, default="")
    is_curated = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 헬퍼 클래스 사용
    objects = UserManager()

	# 사용자의 username field는 email으로 설정 (이메일로 로그인)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    class Meta:
        verbose_name = "유저 관리"
        verbose_name_plural = "유저 목록 관리"


