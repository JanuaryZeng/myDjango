from django.db import models

# Create your models here.
from django.db import models

#import pymysql

class lovertable(models.Model):
    # 默认id
    loverid = models.IntegerField(max_length=255, null=False)
    # 名字，字符串字段，最大长度36位，默认字符KirisameMarisa，允许为空
    lovernumber = models.CharField(max_length=255, null=False)
    # 年龄，整型字段，最大长度5，不允许位空
    loverpassword = models.CharField(max_length=255, null=False)

    loverdate = models.CharField(max_length=255, null=False)

    moneyout = models.CharField(max_length=255, null=False)

    moneyin = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "lovertable"
