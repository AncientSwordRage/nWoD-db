from django.contrib.auth.models import User
from rest_framework import serializers
from characters.mage.models import Mage


class MageSerializer(serializers.ModelSerializer):
    player = serializers.ReadOnlyField(source='player.username')

    class Meta:
        model = Mage
        fields = ('id', 'player', 'name', 'created_date', 'updated_date', 'published_date',
                  'sub_race', 'faction', 'power_level', 'energy_trait', 'virtue', 'vice', 'morality', 'size',)


class UserSerializer(serializers.ModelSerializer):
    mage_by_user = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Mage.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'mage_by_user')
