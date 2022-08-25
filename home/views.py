from django.shortcuts import render
from accounts.models import Core, Developer
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import Testimonial, Gallery
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import GallerySerializer, TestimonialSerializer
from events.models import Event


# Create your views here.
@xframe_options_exempt
def index(request):

    events =  Event.objects.filter(publish = True)
    limit = 3
    if len(events) >  limit:

        events = events[:limit]

    return render(request, 'home/index.html', {'events':events})
 
@xframe_options_exempt
def caPage(request):
     return render(request, 'home/ca.html')

@xframe_options_exempt
def commingSoon(request):
    return render(request, 'home/coming_soon.html')

@xframe_options_exempt
def team(request):
    #get list of objects
    cores = Core.objects.all().order_by('work')
    #pis =  Core.objects.filter(github='2')
    #treasurers = Core.objects.filter(github='3')
    developers = Developer.objects.all()

    context = {'cores':cores,'developers':developers}

    return render(request, 'home/team.html', context)

@xframe_options_exempt
def previous_spons(request):
    #filter on desig equals Sponsorship Head
    cores = Core.objects.filter(designation='Sponsorship Head')
    context = {'cores':cores}
    return render(request, 'home/previous_spons.html', context)

@xframe_options_exempt
def gallery(request):
    return render(request, 'home/gallery.html')

@xframe_options_exempt
def testimonials(request):

    testimonials = Testimonial.objects.all()
    context = {'testimonials':testimonials}

    return render(request, "home/testimonials.html", context)



@api_view(['GET'])
@permission_classes((permissions.AllowAny,))

def images_list(request):
    images = Gallery.objects.all()
    serializer = GallerySerializer(images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,)) 

def livestream_details(request):

  links = Testimonial.objects.filter(pk=1)

  if links:
      link = Testimonial.objects.get(pk=1)
      serializer = TestimonialSerializer(link)
      return Response(serializer.data)

  return Response({"msg":"image does not exist"},status=status.HTTP_404_NOT_FOUND)    


@api_view(['GET'])
@permission_classes((permissions.AllowAny,)) 

def image_details(request,pk):

  images = Gallery.objects.filter(image_id=pk)

  if images:
      image = Gallery.objects.get(image_id=pk)
      serializer = GallerySerializer(image)
      return Response(serializer.data)

  return Response({"msg":"image does not exist"},status=status.HTTP_404_NOT_FOUND)


@xframe_options_exempt
def social(request):
    return render(request, 'home/social.html')



def booklet(request):
    return render(request, 'home/booklet.html')

def blog(request):
    return render(request, 'home/blog.html')

def aarohi_over_the_years(request):
    return render(request, 'home/aarohi-over-the-years.html')

@xframe_options_exempt
def error404(request,exception):
    message = "Oops, looks like the page you are looking for does not exist."
    return render(request,"error.html",{'errorcode':404,"message":message})