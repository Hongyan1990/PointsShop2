from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Points(models.Model):
    """
    积分列表
    """
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.CASCADE)
    points_user = models.CharField(null=False, blank=False, max_length=11, verbose_name='电话')
    points = models.IntegerField(default=0, verbose_name='积分')

    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    update_time = models.DateTimeField(null=True, blank=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '积分列表'
        verbose_name_plural = verbose_name
        unique_together = ("user", "points_user")

    def __str__(self):
        return self.name
