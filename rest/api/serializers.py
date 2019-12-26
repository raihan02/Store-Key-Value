from rest_framework import serializers
from .models import variable

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = variable
        fields = "__all__"
