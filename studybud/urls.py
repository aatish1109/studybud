
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static

 
#this is the root url directory which will now direct to the base urls of the app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('api/',include('base.api.urls'))

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)