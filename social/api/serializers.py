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
            'user_id' : review.user.id
        }

        return details

'''
{
    "id": "b73f9c7b-d1ec-4a7a-964a-0bfd13dc4a58",
    "movie_id": 676705,
    "body": "Good Morning",
    "updated": "2022-03-21T04:20:10.085894Z",
    "created": "2022-03-21T04:20:10.085894Z",
    "user": 1
}
'''