from datetime import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Points

class PointsSerializer(serializers.ModelSerializer):
    """
    购物车
    """
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    def update(self, instance, validated_data):
        instance.points = validated_data['points']
        instance.update_time = datetime.now()
        instance.save()
        return instance

    class Meta:
        model = Points
        validators = [
            UniqueTogetherValidator(
                queryset=Points.objects.all(),
                fields=('user', 'points_user'),
                message="该用户已存在"
            )
        ]
        fields = '__all__'
