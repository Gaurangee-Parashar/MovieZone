import uuid
from warnings import catch_warnings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from social.models import Review
from .serializers import ReviewSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/get_reviews/<movie_id>',
        'POST /api/new_review/body=<>&movie_id=<>',
        'DELETE /api/delete_review/<review_id>'
    ]

    return Response(routes)

# Reviews

@api_view(['GET'])
def getReviews(request, id):
    reviews = Review.objects.filter(movie_id=id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def newReview(request):
    if request.method == 'POST':
        review = Review.objects.create(
            user = request.user,
            movie_id = request.POST.get('movie_id'),
            id=str(uuid.uuid4()),
            body = request.POST.get('body')
        )
        serializer = ReviewSerializer(review, many=False)
        return Response(serializer.data)    

@api_view(['DELETE'])
def deleteReview(request, id):
    if request.method == 'DELETE':
        review = Review.objects.get(id=id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

