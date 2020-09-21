from django.db import models
from core import models as core_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """ Review Model Definition """

    review = models.TextField()
    accurancy = models.IntegerField()
    commuication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accurancy
            + self.commuication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)  # 소수점 이하 둘째 자리까지 표시

    # rating_average.short_description = "Avg." # revies.admin list_display 대체 방법
