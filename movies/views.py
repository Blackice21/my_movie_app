from django.shortcuts import render, redirect
<<<<<<< HEAD
from .models import Movie
from django.contrib import messages


def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_result = Movie.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_result': search_result}
=======
from .models import Movies
from django.contrib import messages


# Create your views here.

def home_page(request):
    user_query = str(request.GET.get('query', ''))
    search_results = Movies.objects.filter(name__icontains=user_query)
    stuff_for_frontend = {'search_results': search_results}
>>>>>>> step_0_start
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
<<<<<<< HEAD
            
            response = Movie.objects.create(
                name=data.get('name'),
                picture=data.get('picture'),
                rating=data.get('rating'),
                notes=data.get('notes'),

            )
            messages.success(request, 'New movie added: {}'.format(data.get('name')))
        except Exception as e:
            messages.warning(
                request, 'Got an error when trying to create new movie: {}'.format(e))
    return redirect('/')

=======
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


>>>>>>> step_0_start
def edit(request, movie_id):
    if request.method == 'POST':
        data = {
            'name': request.POST.get('name'),
            'picture': request.POST.get('picture'),
            'rating': int(request.POST.get('rating')),
            'notes': request.POST.get('notes')
        }
        try:
<<<<<<< HEAD
            movie_obj = Movie.objects.get(id=movie_id)
=======
            movie_obj = Movies.objects.get(id=movie_id)
>>>>>>> step_0_start
            movie_obj.name = data.get('name')
            movie_obj.picture = data.get('picture')
            movie_obj.rating = data.get('rating')
            movie_obj.notes = data.get('notes')
            movie_obj.save()
<<<<<<< HEAD
            messages.success(request, f"Movie updated - {data.get('name')}")
        except Exception as e:
            messages.warning(
                request, 'Got an error when trying to update movie: {}'.format(e))
        return redirect('/')

def delete(request, movie_id):
    try:
        movie_obj = Movie.objects.get(id=movie_id)
        movie_name = movie_obj.name
        movie_obj.delete()
        messages.warning(request, 'Deleted movie: {}'.format(movie_name))
    except Exception as e:
        messages.warning(request, 'Got an error when trying to delete a movie: {}'.format(e))
    return redirect('/')
=======
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
>>>>>>> step_0_start
