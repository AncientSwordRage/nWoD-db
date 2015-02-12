from django.contrib.auth.models import User
from rest_framework import serializers
from characters.mage.models import Mage


class MageSerializer(serializers.ModelSerializer):
    player = serializers.ReadOnlyField(source='player.username')
    arcana = serializers.StringRelatedField(many=True)
    mental_attributes = serializers.StringRelatedField(many=True)
    physical_attributes = serializers.StringRelatedField(many=True)
    social_attributes = serializers.StringRelatedField(many=True)
    skills = serializers.StringRelatedField(many=True)

    class Meta:
        model = Mage
        fields = ('id', 'player', 'name', 'sub_race', 'faction', 'is_published',
                  'power_level', 'energy_trait', 'virtue', 'vice', 'morality', 'size',
                  'arcana', 'mental_attributes', 'physical_attributes', 'social_attributes', 'skills')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    mage_by_user = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Mage.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'mage_by_user')
