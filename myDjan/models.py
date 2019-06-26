from django.db import models

# Create your models here.
from django.db import models

class lovertable(models.Model):
    # 默认id
    loverid = models.CharField(max_length=100, primary_key=True)
    # 名字，字符串字段，最大长度36位，默认字符KirisameMarisa，允许为空
    # 年龄，整型字段，最大长度5，不允许位空
    loverpassword = models.CharField(max_length=100, null=False)
    loverdate = models.CharField(max_length=100)
    moneyout = models.CharField(max_length=100, default='0')
    moneyin = models.CharField(max_length=100, default='0')
    class Meta:
        db_table = "lovertable"

class moneytypetable(models.Model):
    moneytypeid = models.CharField(max_length=255, null=False,primary_key=True)
    moneytypeicon =  models.CharField(max_length=255, null=False)
    moneydirction = models.CharField(max_length=255, null=False)
    class Meta:
        db_table = "moneytypetable"

class moneychangetable(models.Model):

    moneychangeid  = models.AutoField(primary_key=True)
    loverid = models.ForeignKey(lovertable,on_delete=models.CASCADE,db_column="loverid")
    moneytypeid = models.ForeignKey(moneytypetable,on_delete=models.CASCADE,db_column="moneytypeid")
    moneydate = models.CharField(max_length=255, null=False)
    moneynumber = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "moneychangetable"







