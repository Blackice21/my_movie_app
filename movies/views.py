from django.shortcuts import render, redirect
from .models import Movies
from django.contrib import messages


# Create your views here.

def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_results = Movies.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_results': search_results}
    return render(request, 'movies/movies_stuff.html', stuff_for_frontend)


def create(request):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            response = Movies.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                rating=data.get('rating'),
                notes=data.get('notes')
            )
            messages.success(request, 'New Movie added: {}'.format(data.get('name')))
        except Exception as e:
            messages.warning(request, 'Could not add movie ' + data.get('name'))
    return redirect('/')


def edit(request, movie_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
            movie_obj = Movies.objects.get(id=movie_id)
            movie_obj.name = data.get('name')
            movie_obj.picture = data.get('picture')
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            movie_obj.save()
            messages.success(request, 'Movie updated!')
        except Exception as e:
            messages.warning(request, f'could not update movie')
        return redirect('/')


def delete(request, movie_id):
    try:
        movie_obj = Movies.objects.get(id=movie_id)
        mn = movie_obj.name
        movie_obj.delete()
        messages.success(request, 'Movie deleted: {}'.format(mn))
    except:
        messages.warning(request, f'Movie could not be deleted')
    return redirect('/')
