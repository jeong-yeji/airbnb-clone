from django.db import models
from core import models as core_models
from django_countries.fields import CountryField

# from users import models as user_models

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """" Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)
    # python은 위에서부터 코드를 읽기 때문에 "" 없이 쓰려면 class Room 아래에 있어야 함

    def __str__(self):
        return self.caption


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
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )  # 일대다관계
    # on_delete=models.CASCADE : host 삭제하면 host에 포함 된 room도 삭제됨
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )  # 다대다관계
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def total_rating(self):
        all_reviews = self.reviews.all()  # reviews는 related_name
        all_ratings = 0
        if len(all_reviews)>0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return all_ratings / len(all_reviews)
        return 0
