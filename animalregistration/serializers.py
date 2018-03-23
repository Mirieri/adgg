from rest_framework import serializers

from .models import Reg02Maininfo, Reg01Lkpmaindistrict, Reg04Maininfo


class Reg04MaininfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reg04Maininfo
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'animalregistration-detail',
                'lookup_field': 'hh'
            }
        }


class Reg02MaininfoSerializer(serializers.HyperlinkedModelSerializer):
    hh_district = serializers.HyperlinkedRelatedField(
        view_name='district-detail',
        read_only=True,
        lookup_field='maindistrict_des'
    )
    reg04maininfo = serializers.HyperlinkedIdentityField(
        view_name='animalregistration-detail',
        many=True,
        read_only=True,
        lookup_field='hh'
    )

    class Meta:
        model = Reg02Maininfo
        fields = '__all__'


class Reg01LkpmaindistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reg01Lkpmaindistrict
        fields = '__all__'
        extra_kwargs = {
            'url': {
                'view_name': 'district-detail',
                'lookup_field': 'maindistrict_des'
            }
        }
