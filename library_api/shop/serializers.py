from rest_framework import serializers
from .models import Gift, Merchandise

class GiftSerializer(serializers.ModelSerializer):
    presenter_name = serializers.CharField(source = "presenter.name", read_only=True)
    class Meta:
        model = Gift
        fields = ['id', 'name', 'presenter','presenter_name', 'description']

class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = "__all__"