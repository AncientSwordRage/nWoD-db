from django.contrib.auth.models import User
from rest_framework import serializers
from characters.mage.models import Mage


class EnumField(serializers.Field):

    """
    Enum objects are serialized into " 'label' : value " notation
    """

    def to_representation(self, obj):
        return "'{0}': {1} ".format(obj.all()[0].__str__(), obj.all()[0].current_value)


class EnumListField(serializers.ListField):
    child = EnumField()


class MageSerializer(serializers.ModelSerializer):
    player = serializers.ReadOnlyField(source='player.username')
    arcana = serializers.StringRelatedField(many=True)
    mental_attributes = EnumListField()
    physical_attributes = EnumListField()
    social_attributes = EnumListField()
    mental_skills = EnumListField()
    physical_skills = EnumListField()
    social_skills = EnumListField()

    class Meta:
        model = Mage
        fields = ('id', 'player', 'name', 'sub_race', 'faction', 'is_published',
                  'power_level', 'energy_trait', 'virtue', 'vice', 'morality', 'size',
                  'arcana', 'mental_attributes', 'physical_attributes', 'social_attributes',
                  'mental_skills', 'physical_skills', 'social_skills')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    mage_by_user = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Mage.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'mage_by_user')
