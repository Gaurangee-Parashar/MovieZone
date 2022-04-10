from rest_framework.serializers import ModelSerializer, SerializerMethodField
from social.models import Review

class ReviewSerializer(ModelSerializer):
    user = SerializerMethodField('get_user_details')
    class Meta:
        model=Review
        fields = ['id', 'movie_id', 'body', 'created', 'updated', 'user']

    def get_user_details(self, review):
        details = {
            'username' : review.user.username,
            'user_id' : review.user.id,
            'profile_pic_url' : review.user.profile.profile_pic.url
        }

        return details
