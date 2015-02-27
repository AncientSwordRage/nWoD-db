from django.contrib.auth.models import User
from rest_framework import serializers
from characters.mage.models import Mage, CharacterArcanumLink


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
            return {str(arcana): arcana.current_value for arcana in obj.linked_arcana.all()}

    attributes = serializers.SerializerMethodField('character_attribute')
    skills = serializers.SerializerMethodField('character_skill')

    def character_attribute(self, obj):
        character_attribute_fields = {}
        character_attribute_fields['mental'] = {str(trait_item.get()): trait_item.get().current_value
                                                for trait_item in obj.mental_attributes}
        character_attribute_fields['physical'] = {str(trait_item.get()): trait_item.get().current_value
                                                  for trait_item in obj.physical_attributes}
        character_attribute_fields['social'] = {str(trait_item.get()): trait_item.get().current_value
                                                for trait_item in obj.social_attributes}
        return character_attribute_fields

    def character_skill(self, obj):
        character_skill_fields = {}
        character_skill_fields['mental'] = {str(trait_item.get()): trait_item.get().current_value
                                            for trait_item in obj.mental_skills}
        character_skill_fields['physical'] = {str(trait_item.get()): trait_item.get().current_value
                                              for trait_item in obj.physical_skills}
        character_skill_fields['social'] = {str(trait_item.get()): trait_item.get().current_value
                                            for trait_item in obj.social_skills}
        return character_skill_fields

    class Meta:
        model = Mage
        fields = ('id', 'player', 'name', 'sub_race', 'faction', 'is_published',
                  'power_level', 'energy_trait', 'virtue', 'vice', 'morality', 'size',
                  'arcana', 'attributes', 'skills')
        depth = 1


class UserSerializer(serializers.ModelSerializer):
    mage_by_user = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Mage.objects.all())
    mage_last_updated = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'mage_by_user', 'mage_last_updated',)

    def get_mage_last_updated(self, obj):
        latest_mage = obj.mage_by_user.latest('updated_date')
        return latest_mage.updated_date
