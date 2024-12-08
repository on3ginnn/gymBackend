from rest_framework import serializers

import aboniment.models


class AbonimentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboniment.models.Aboniment
        fields = ['title', 'duration', 'owner']


class AbonimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboniment.models.Aboniment
        fields = ['id', 'title', 'duration', 'owner']