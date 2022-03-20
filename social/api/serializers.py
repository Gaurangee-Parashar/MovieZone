from pyexpat import model
from attr import fields
from rest_framework.serializers import ModelSerializer
from social.models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'