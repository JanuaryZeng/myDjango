from .models import lovertable
from rest_framework import serializers

# 名字随意
class lovertableSerializer(serializers.ModelSerializer):
    class Meta:
        # 对应类名
        model = lovertable
        # 各个字段，其中_id是默认id字段
        fields = ('loverid', 'lovernumber','loverpassword','loverdate','moneyout','moneyin')

