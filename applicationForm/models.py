from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django_resized import ResizedImageField
from django.utils import timezone
from image_optimizer.fields import OptimizedImageField
from .manager import UserManager

IMAGE_SIZE = (400, 400)
IMAGE = [1200, 675]


# Basemodel
class BaseModel(models.Model):
    created_at = models.DateTimeField(_('Kiritilgan sana'), auto_now_add=True)
    updated_at = models.DateTimeField(_('O\'zgartirilgan sana'), auto_now=True)

    class Meta:
        abstract = True


# Territory
class Region(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('City'))
    code = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('City / Region')
        verbose_name_plural = _('Cities / Regions')


class District(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('District'))
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name=_(
        'Viloyat'), related_name='districts', null=True ,)
    code = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')


# Main user
class Role(BaseModel):
    USERTYPE = (
        (1, _('superadmin')),
        (2, _('admin')),
        (3, _('manager')),
        (4, _('moderator')),
        (5, _('top_manager')),
        (6, _('customer')),
        (7, _('dispatcher')),
        (8, _('worker')),
        (9, _('cashier')),
    )
    name = models.CharField(max_length=128)
    user_type = models.IntegerField(
        choices=USERTYPE, verbose_name=_('Lavozim'), default=6)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Lavozim'
        verbose_name_plural = 'Lavozimlar'


class BaseUser(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("Bu foydalanuvchi nomi allaqachon mavjud."),
        },
    )

    phone_regex = RegexValidator(regex=r'^\d{9}$', message=_(
        "13-ta raqamgacha ruxsat berilgan."))
    full_name = models.CharField(_('To\'liq ism'), max_length=128, blank=True)
    email = models.EmailField(_('Email'), blank=True, null=True)
    active = models.BooleanField(_('Aktiv'), default=True),
    date_joined = models.DateTimeField(
        _('Ro\'yxatdan o\'tgan sana'), default=timezone.now)
    last_login = models.DateTimeField(
        _('Oxirgi aktiv holati'), null=True, blank=True, default=timezone.now)
    phone = models.CharField(_('Telefon raqam'), max_length=60, validators=[
                             phone_regex], null=True, blank=True)
    avatar = OptimizedImageField(verbose_name=_('Rasm'), optimized_image_output_size=IMAGE_SIZE,
                                 optimized_image_resize_method='cover', upload_to='user/%Y/%m', null=True, blank=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('Tuman'))
    device = models.CharField(_('Qurilma'), max_length=500, null=True)
    ip_address = models.CharField(_('IP manzil'), max_length=30, null=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(_('Kiritilgan sana'), auto_now_add=True)
    updated_at = models.DateTimeField(_('O\'zgartirilgan sana'), auto_now=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Tizim Foydalanuvchisi'
        verbose_name_plural = 'Tizim Foydalanuvchilari'

    def __str__(self):
        return f"{self.username} - {self.full_name}"

    @property
    def image_url(self):
        return '%s%s' % (settings.HOST, self.avatar.url) if self.avatar else ''

    def roles(self):
        return self.user_roles.values_list('role__user_type', flat=True)
        # return [item.role.name for item in self.user_roles]

    def region(self):
        return self.district.region if self.district else None


class UserRole(BaseModel):
    base_user = models.ForeignKey(
        BaseUser, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Foydalanuvchi roli')
        verbose_name_plural = _('Foydalanuvchi roli')

    def __str__(self):
        return f"{self.base_user.full_name} - {self.role.name}" or f"{self.id}"


# SETTING
class UserSetting(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, verbose_name=_(
        'Foydalanuvchi'), related_name='setting')
    dark = models.BooleanField(_('Dark'), default=True),
    caching = models.BooleanField(_('Keshlash'), default=True),
    notification = models.BooleanField(_('Xabarnomalar'), default=True),
 

    def __str__(self):
        return f'{self.user.full_name}'

    class Meta:
        verbose_name = _('Sozlama')
        verbose_name_plural = _('Sozlamalar')


