import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.user.models import User
from apps.user.pwd_encoder import get_md5


class UserSerializer(serializers.ModelSerializer):

    # email作为账户名, 需要唯一性验证
    email = serializers.EmailField(
        # 必须
        required=True,
        # 不允许空
        allow_null=False,
        # 唯一性校验
        validators=[UniqueValidator(queryset=User.objects.all(), message="用户已存在")]
    )

    # 时间格式化
    birthday = serializers.DateTimeField('%Y-%m-%d %H:%M:%S')
    create_time = serializers.DateTimeField('%Y-%m-%d %H:%M:%S', required=False)

    # 在调用save()时自动被调用，在数据存储之前进行加工
    def create(self, validated_data):
        # 密码md5加密
        validated_data['password'] = get_md5(validated_data['password'])

        # 取当前时间为注册时间
        validated_data['create_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        result = User.objects.create(**validated_data)
        return result

    class Meta:
        model = User
        fields = "__all__"
        # 创建用户后密码不返回给前端
        extra_kwargs = {'password': {'write_only': True}}