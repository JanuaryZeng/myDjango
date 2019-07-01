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


class notetable(models.Model):
    noteid  = models.AutoField(primary_key=True)
    loverid = models.ForeignKey(lovertable,on_delete=models.CASCADE,db_column="loverid")
    moneytypeid = models.ForeignKey(moneytypetable,on_delete=models.CASCADE,db_column="moneytypeid")
    notedate = models.CharField(max_length=255, null=False)
    notetext = models.CharField(max_length=255, null=False)
    notestatus = models.CharField(max_length=255, null=False)#用来判断是消费还是代办的，还有完成的

    class Meta:
        db_table = "notetable"

class usertable(models.Model):

    userid = models.AutoField(primary_key=True)
    loverid = models.ForeignKey(lovertable,on_delete=models.CASCADE,db_column="loverid")
    usergender = models.CharField(max_length=10,default="man")
    username = models.CharField(max_length=255,default="user")
    usericon = models.CharField(max_length=255,null=True)
    userborn = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = "usertable"


class friendtable(models.Model):

    friendid = models.AutoField(primary_key=True)
    loverid = models.ForeignKey(lovertable,on_delete=models.CASCADE,db_column="loverid")
    usergender = models.CharField(max_length=10,default="man")
    frienddate = models.CharField(max_length=255, null=False)
    friendphotos1 = models.CharField(max_length=255, null=True)
    friendphotos2 = models.CharField(max_length=255, null=True)
    friendphotos3 = models.CharField(max_length=255, null=True)
    friendphotos4 = models.CharField(max_length=255, null=True)
    friendtext = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "friendtable"


