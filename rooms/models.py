from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """" Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    pass


# room이 언제 등록, 업데이트 됐는지 확인하는 기능 만들고 싶음
# 그럼 timestamp 기능 추가해야됨
# 근데 이 기능이 rooms에서만 쓰이는게 아니라 lists, reservations, reviews에서도 쓰이니까
# TimeStampedModel을 만들어서 작업을 간단하게 하자!
# 근데 TimeStampedModel은 db에 등록될 필요는 없으니까 Abstract Model로 설정
class Room(core_models.TimeStampedModel):

    """ Rooms Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)  # 일대다관계
    room_type = models.ManyToManyField(RoomType, blank=True)  # 다대다관계

    def __str__(self):
        return self.name
