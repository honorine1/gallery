from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Image
import datetime as dt



# def welcome(request):
  
#     return render (request, 'welcome.html')

def index(request):
    photos = Image.get_all_photos()
    return render (request, 'all_photos/index.html',{"photos":photos})


def photos_of_day(request):
   
    date = dt.date.today()
    photos = Image.todays_photos()
    return render(request, 'all_photos/today_photo.html', {"date": date,"photos":photos})
  
    
    
def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
    

    
   # View Function to present news from past days

def search_images(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category_name(search_term)
        message = f"{search_term}"

        return render (request, 'all_photos/search.html',{"message":message, "images":searched_images})

    else:
        message = "you haven't searched for any term"
        return render(request,'all_photos/search.html',{"message":message})




def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all_photos/image.html", {"image":image})

