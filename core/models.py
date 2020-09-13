from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  # 생성 시 자동 시간 저장
    updated = models.DateTimeField(auto_now=True)  # 저장(업데이트) 시 자동 시간 저장

    # TimeStampedModel을 abstract model로 설정
    # abstarct model : model이지만 db에 나타나지 않는 model
    class Meta:
        abstract = True
