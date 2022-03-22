import requests
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from social.models import Review, ReviewReply

# Home page 
def coming_soon(KEY):
    response = requests.get(f"https://api.themoviedb.org/3/movie/upcoming?api_key={KEY}").json().get('results')
    return response

def most_popular(KEY):
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={KEY}").json().get('results')
    return response

@login_required(login_url='login')
def home(request):
    KEY = "08e732edbde3ebbc312edf9503748b58"
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    movies_coming_soon = coming_soon(KEY)
    most_popular_movies = most_popular(KEY)
    reviews = Review.objects.all().order_by('-created')
    context = {'movies_coming_soon' : movies_coming_soon, 'most_popular_movies' : most_popular_movies, 'reviews' : reviews}
    return render(request, 'base/home.html', context)

# Search 

def search(request):
    name = request.GET.get('query')
    try:
        KEY = "08e732edbde3ebbc312edf9503748b58"
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={KEY}&query={name}").json()
        movies = response.get('results')
        movie_details = []

        for movie in movies:
            
            movie_details.append({
                "id" : movie.get('id'),
                "Title" : movie.get('title'),
                "Year" : movie.get('release_date'),
                "Image" : f"https://image.tmdb.org/t/p/w1280/{movie.get('poster_path')}",
                'Overview' : movie.get('overview')
            })
            
        context = {"movie_details": movie_details}
        return render(request, 'base/search_results.html', context)
    except:
        return render(request, 'Error.html')


# Movie details page 

def get_reviews(id):
    try:
        reviews = Review.objects.filter(movie_id=id).order_by('-created')
    except:
        reviews = None
    return reviews

def get_review_replies(review):
    try: 
        replies = ReviewReply.objects.get(parent_review=review)
    except:
        replies = None
    return replies

def movies(request, id):
    KEY = "08e732edbde3ebbc312edf9503748b58"
    reviews = get_reviews(id)
    review_replies = []
    for review in reviews:
        review_replies.append(get_review_replies(review))
    movie_details = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={KEY}').json()
    movie_cast = requests.get(f"https://api.themoviedb.org/3/movie/{id}/credits?api_key={KEY}").json()['cast']

    context = {'movie_details' : movie_details, 'movie_cast' : movie_cast, 'reviews' : reviews, 'review_replies' : review_replies}
    return render(request, 'base/movies.html', context)

# Person details

def person(request, id):
    KEY = "08e732edbde3ebbc312edf9503748b58"
    person_details = requests.get(f"https://api.themoviedb.org/3/person/{id}?api_key={KEY}").json()
    context = {'person_details' : person_details}
    return render(request, 'base/person.html', context)
