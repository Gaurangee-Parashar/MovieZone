from webbrowser import get
import requests
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Home page 
def coming_soon(KEY):
    response = requests.get(f"https://api.themoviedb.org/3/movie/upcoming?api_key={KEY}").json().get('results')
    return response

def most_popular(KEY):
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={KEY}").json().get('results')
    return response

def trending(KEY):
    response = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={KEY}").json().get('results')
    return response

@login_required(login_url='login')
def home(request):
    KEY = "08e732edbde3ebbc312edf9503748b58"
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    if q == 'trending':
        results = trending(KEY)
        context = {'results' : results, 'q' : q}
        return render(request, 'base/category.html', context)
    if q == "popular":
        results = most_popular(KEY)
        context = {'results' : results, 'q' : q}
        return render(request, 'base/category.html', context)
    
    movies_coming_soon = coming_soon(KEY)
    most_popular_movies = most_popular(KEY)
    context = {'movies_coming_soon' : movies_coming_soon, 'most_popular_movies' : most_popular_movies}
    return render(request, 'base/home.html', context)

# Search 

def search(request, type):
    KEY = "08e732edbde3ebbc312edf9503748b58"
    name = request.GET.get('query')
    movies = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={KEY}&query={name}").json().get('results')
    tvshows = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={KEY}&query={name}").json().get('results')
    persons = requests.get(f"https://api.themoviedb.org/3/search/person?api_key={KEY}&query={name}").json().get('results')

    search_results_no = {'movies' : len(movies), 'tv' : len(tvshows), 'persons' : len(persons)}
    # Movie
    if type == 'movie':
        movie_details = []
        for movie in movies:
            
            movie_details.append({
                "id" : movie.get('id'),
                "title" : movie.get('title'),
                "year" : movie.get('release_date'),
                "image" : f"https://image.tmdb.org/t/p/w1280/{movie.get('poster_path')}",
                'overview' : movie.get('overview')
            })
            
        context = {"results": movie_details,  "name" : name, "search" : "movie", "search_results_no" : search_results_no}
        return render(request, 'base/search_results.html', context)
    # TV
    elif type == 'tv':
        tvshow_details = []
        for show in tvshows:
            
            tvshow_details.append({
                "id" : show.get('id'),
                "title" : show.get('original_name'),
                "year" : show.get('first_air_date'),
                "image" : f"https://image.tmdb.org/t/p/w1280/{show.get('poster_path')}",
                'overview' : show.get('overview')
            })

        context = {"results" : tvshow_details, "name" : name, "search" : "tv", "search_results_no" : search_results_no}
        return render(request, 'base/search_results.html', context)
    # Person
    elif type == 'person':
        person_details = []
        for person in persons:
            
            person_details.append({
                "id" : person.get('id'),
                "name" : person.get('name'),
                "known_for_department" : person.get('known_for_department'),
                "known_for" : person.get('known_for'),
                "image" : f"https://image.tmdb.org/t/p/w1280/{person.get('profile_path')}",
            })

        context = {"results" : person_details, "name" : name, "search" : "person", "search_results_no" : search_results_no}
        return render(request, 'base/search_results.html', context)        

# Movie details page 

def get_reviews(id):
    try:
        reviews = requests.get(f"http://127.0.0.1:8000/api/get_reviews/{id}").json()

    except:
        reviews = None
    return reviews

def movies(request, id):
    KEY = "08e732edbde3ebbc312edf9503748b58"
    reviews = get_reviews(id)
    movie_details = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={KEY}').json()
    movie_cast = requests.get(f"https://api.themoviedb.org/3/movie/{id}/credits?api_key={KEY}").json()['cast']
    movie_trailers = requests.get(f"https://api.themoviedb.org/3/movie/{id}/videos?api_key={KEY}").json()['results']

    context = {'movie_details' : movie_details, 'movie_cast' : movie_cast, 'movie_trailers' : movie_trailers, 'reviews' : reviews,}
    return render(request, 'base/movies.html', context)

# Person details

def person(request, id):
    KEY = "08e732edbde3ebbc312edf9503748b58"
    person_details = requests.get(f"https://api.themoviedb.org/3/person/{id}?api_key={KEY}").json()
    context = {'person_details' : person_details}
    return render(request, 'base/person.html', context)
