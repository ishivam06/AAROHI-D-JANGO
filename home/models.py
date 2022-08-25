from django.db import models

# Create your models here.
class Testimonial(models.Model):

    name = models.CharField(max_length=200)
    photo = models.FileField(upload_to="alumni_testimonial", null=True)
    content = models.TextField()
    batch = models.CharField(max_length=100)
    linked_in =  models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):

        return self.name


def get_default_gallery_id():

    images = Gallery.objects.all()
    ids = []
    #not empty
    if images:

        #colect ids
        for image in images:
            ids.append(image.image_id)

        #id of last object
        last_id = ids[len(ids)-1]

        #return next id
        return last_id + 1

    else:

        return 1


class Gallery(models.Model):

    #assign last objects id
    #dont reply on deafult pk as on deletion it will autoincrement
    image_id = models.IntegerField(default=get_default_gallery_id, primary_key=True)
    image =  models.FileField(upload_to="gallery")
    description = models.CharField(max_length=200, null=True, blank=True)
