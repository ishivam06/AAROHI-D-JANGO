# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from exhibitions.models import Exhibit


def list_blogs(request):

    exhibits = Exhibit.objects.filter(date__month='04')
    context = {
        "exhibits":exhibits
    }
    return render(request,'blogs/blogs_list.html',context)

def list_photos(request):

    exhibits = Exhibit.objects.filter(date__month='03')
    context = {
        "exhibits":exhibits
    }
    return render(request,'blogs/shutterbug.html',context)

def blog_details(request,id):
    
    if(Exhibit.objects.filter(pk = id)):
        exhibit = Exhibit.objects.get(pk = id)
        return render(request,'blogs/blog_details.html',context = {"blog":exhibit})
    
    return render(request,'error.html',{'errorcode':404,'message':'Not found'})

    

def like_blog(request,id):
    if request.is_ajax and request.method == "GET":
        exhibit = Exhibit.objects.get(pk = id)
        exhibit.likes = exhibit.likes + 1
        likes = exhibit.likes
        exhibit.save()

        return JsonResponse({'likes':likes}, status = 200)
    
    return JsonResponse({}, status = 500)
