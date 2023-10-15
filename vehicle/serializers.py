from rest_framework import serializers

from vehicle.models import Car, Moto, Mileage
from vehicle.validators import TitleValidator


class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_mileage = serializers.IntegerField(source='mileage_set.all.first.mileage', read_only=True)
    mileages = MileageSerializer(source='mileage_set.all', many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'
        validators = [
            TitleValidator(field='title'),
            serializers.UniqueTogetherValidator(fields=['title', 'description'], queryset=Car.objects.all())
        ]


class MotoSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField(read_only=True)

    def get_last_mileage(self, instance):
        if instance.mileage.all().first():
            return instance.mileage.all().first().mileage
        return 0

    class Meta:
        model = Moto
        fields = '__all__'
        validators = [TitleValidator, ]


class MotoMileageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Mileage
        fields = ['mileage', 'year', 'moto', ]


class MotoCreateSerializer(serializers.ModelSerializer):
    mileage = MileageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def create(self, validated_data):
        mileage = validated_data.pop('mileage')

        moto_item = Moto.objects.create(**validated_data)

        for mileage_item in mileage:
            Mileage.objects.create(moto=moto_item, **mileage_item)

        return moto_item

