# Add image column in model 
1. To upload the image in database then create column for image and data type of column is **ImageField**    
2. The column is create in model.    
3. apply makemigartions and migrate.   
``` 
Example  
 image = models.ImageField(upload_to='profile_images', blank=True)
```    
# Settings.py for url path , static file store location at production  
1. add variable `MEDIA_URL = '/media/'` for url path.  
2. add variable `MEDIA_ROOT = os.path.join(BASE_DIR, 'tutorial/media')` for production.    
3. At production time tutorial dir create automatically `media/profile_images/image_name_extension`  

# when image upload then automatically folder create in app and image store  
1. When open admin page and after that  choose the image for uploading.     
2. The `upload_to='profile_images` profile_images folder create and image is save.    

# saving files uploaded by use during development  
1. from django.conf import settings   
2. from django.conf.urls.static import static   
3. define MEDIA_URL and document_root  
``` 
Example 
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts') ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```  

# show images using template  
1. <img src="{{ user.userprofile.image.url }}" width="240">  
2. Use html tag to show image.  
