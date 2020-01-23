from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
     url(r'^signup/',views.signup,name='signup'),
    url('^$',views.home,name='home'),
    url('^profile/',views.profile, name='profile')
    # url(r'^images/',views.add_image,name='Image'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
