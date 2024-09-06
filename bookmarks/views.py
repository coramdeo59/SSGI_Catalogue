from django.shortcuts import render, redirect
from .models import Bookmark
from sidebarquery.models import ssgi
from django.contrib.auth.models import User
import os

user_model = User()

def bookmark_image(request, id):
    if request.method == "GET":
        context = {
            'id': id
        }
        return render(request, 'bookmark/bookmark_image.html', context)
    else:
        desc = request.POST['desc']
        image_instance = ssgi.objects.filter(id=id)[0]
        bookmark = Bookmark.objects.create(user=request.user, image=image_instance, description=desc)
        return redirect('bookmark-list')

def bookmark_list(request):
    def check_thumb_and_ssgi(bookmarks, thumbnails):
        final = []
        for bookmark in bookmarks:
            for thumbnail in thumbnails:
                if bookmark.image_id == thumbnail['id']:
                    final.append(thumbnail)
        return final
    thumbnails = []
    foldercursor = ssgi.objects.filter().values()
    for folder_row in foldercursor:
        folder=folder_row.get('folder')
        id=folder_row.get('id')
        folderdirctories=os.listdir(folder)
        path = folder
        for file in folderdirctories:
            if file.endswith('THUMB.jpg'):
                thumbnails.append({'id': id, 'path': path +"\\"+file })
    context = {
        'bookmarks': Bookmark.objects.filter(user_id=request.user.id),
        'thumbnails': thumbnails,
        'final': check_thumb_and_ssgi(Bookmark.objects.filter(user_id=request.user.id),thumbnails)
    }

    return render(request, 'bookmark/bookmark.html', context)


