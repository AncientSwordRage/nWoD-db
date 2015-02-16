from django.contrib.auth.models import User
from rest_framework import serializers
from characters.mage.models import Mage, CharacterArcanumLink


class TraitField(serializers.Field):

    """
    Trait objects are serialized into " 'label' : value " notation
    """

    def to_representation(self, obj):
        return {str(trait_item.get()): trait_item.get().current_value for trait_item in obj}


class TraitRelatedField(serializers.Field):

    def to_representation(self, obj):
        return {str(obj): item.current_value for item in obj.all()}


class CharacterArcanumLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = CharacterArcanumLink
        fields = ('current_value', 'arcana')


class MageSerializer(serializers.ModelSerializer):
    player = serializers.ReadOnlyField(source='player.username')
    arcana = serializers.SerializerMethodField()

    def get_arcana(self, obj):
        if obj:
            return {str(x): CharacterArcanumLink.objects.filter(arcana=x).get().current_value
                    for x in obj.arcana.all()}
    mental_attributes = TraitField()
    physical_attributes = TraitField()
    social_attributes = TraitField()
    mental_skills = TraitField()
    physical_skills = TraitField()
    social_skills = TraitField()

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
