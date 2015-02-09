from rest_framework import serializers
from characters.mage.models import Mage


class MageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mage
