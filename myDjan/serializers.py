from .models import lovertable, moneytypetable, moneychangetable
from rest_framework import serializers

class moneychangetableSerializer(serializers.ModelSerializer):
    serializers.CharField(source='FK.字段')
    class Meta:
        # 对应类名
        model = moneychangetable
        # 各个字段，其中_id是默认id字段
        # fields = ('moneychangeid', 'moneydate','moneynumber','loverid','moneytypeid')
        fields = "__all__"

# 名字随意
class lovertableSerializer(serializers.ModelSerializer):
    class Meta:
        # 对应类名
        model = lovertable
        # 各个字段，其中_id是默认id字段
        fields = ('loverid','loverpassword','loverdate','moneyout','moneyin')
        # fields = "__all__"


class moneytypetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = moneytypetable
        # fields = ('moneytypeid', 'moneytypeicon','moneydirction')
        fields = "__all__"
# try:
#     mon_change_obj = moneychangetable.objects.get(loverid_id=data['loverid'])
# except moneychangetable.DoesNotExist:
#     return Response('参数不存在')
#
# ser = moneychangetableSerializer(instance=mon_change_obj ,many=False)
# return Response(ser.data, status=status.HTTP_200_ok)
#
# class moneychangetableSerializerc(serializers.ModelSerializer):
#     """金额变化表的序列化""""
#
#     class Meta:
#         model = moneychangetable
#         fields = "__all__"  # "__all__" 意思就是取出全部的字段

