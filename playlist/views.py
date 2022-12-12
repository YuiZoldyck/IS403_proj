#git test 123

from django.shortcuts import render, redirect
from .models import Songs, Category

# Create your views here.
# main page
def indexPageView(request):
    return render(request, 'index.html')

# page to view all existing songs in playlist
def viewPageView(request):
    songs = Songs.objects.all().values()
    categories = Category.objects.all()
    context = {
        'data':songs,
        'cats':categories
    }
    return render(request, 'displaySongs.html', {'data':context})

# link to reorder songs within playlist by categories
def reorderTable(request): 
    order = request.GET.get('orderby')
    songs = Songs.objects.all().order_by(order).values()
    categories = Category.objects.all()
    context = {
        'data':songs,
        'cats':categories
    }
    return render(request, 'reorder.html', {'data':context})

# link to add new song into playlist
def createPageView(request):
    return render(request, 'addSong.html')

# link to redirect to home after adding somg
def addRecordView(request):
    if request.method == 'POST':
        name = request.POST['SongName']
        artist = request.POST['Artist']
        album = request.POST['Album']
        year = request.POST['YearReleased']

        song = Songs()

        song.SongName = name
        song.Artist = artist
        song.Album = album
        song.YearReleased = year

        song.save()

    return redirect(viewPageView)

# link to update existing song
def editPageView(request, sid):
    song = Songs.objects.values().get(id=sid)
    context = {
        'data':song
    }
    return render(request, 'editSong.html', {'data':context})

# link to save the new updates to song, redirect to home
def submitChanges(request,sid):
    song = Songs.objects.get(id=sid)

    if request.method == 'POST':
        name = request.POST['SongName']
        artist = request.POST['Artist']
        album = request.POST['Album']
        year = request.POST['YearReleased']

        song.SongName = name
        song.Artist = artist
        song.Album = album
        song.YearReleased = year

        song.save()
    return redirect(viewPageView)
    
# delete song from playlist
def deletePageView(request, sid):
    song = Songs.objects.get(id=sid).delete()
    return redirect(viewPageView)