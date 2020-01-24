from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^signup/',views.signup,name='signup'),
    url('^$',views.home,name='home'),
    # url(r'^sell/gari$',views.sell_gari, name='sell-gari'),
    url(r'^search/',views.search_brand,name='search_brand'),
    url('^profile/',views.profile, name='profile'),
    url(r'^api/gari/$',views.GariList.as_view()),
    url(r'^gari/(\d+)',views.single_gari, name='gari'),
    # url(r'^sell/gari$', views.sell_gari, name='sell-gari'),
    url(r'^used/gari$', views.used_gari, name='used-gari'),
    url(r'^new/gari$', views.new_gari, name='new-gari'),
    # url(r'^images/',views.add_image,name='Image'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
