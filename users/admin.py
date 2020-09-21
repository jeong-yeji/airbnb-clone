from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models  # . 은 지금 폴더와 같은 폴더 의미

# Register your models here.

# admin.site.register(models.User, CustomUserAdmin)
# 아래의 decorator와 같은 의미
# 이건 클래스 끝난 뒤 클래스 바깥에 작성
# admin 패널에서 models.User를 볼거다
# models.User를 control 할 class는 CustomUserAdmin
@admin.register(models.User)  # decorator : class name 바로 위에 있어야 작동?
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    """
    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
    """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
