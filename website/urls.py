from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('towers/',views.towers, name="towers"),
    path('towers/towers-list',views.towers_list, name="towers_list"),
    path('towers/towers-list/<str:site_name>/',views.tower_page,name="tower_page"),
    path('towers/state-list/',views.state_list, name="state_list"),
    path('towers/state-list/<str:address_state>/',views.towers_bystate,name="towers_bystate"),
    path('downloads/',views.downloads, name="downloads"),
    path('collocation/',views.collocation, name="collocation"),
    path('about_us/',views.about_us, name="about_us"),
    path('contact_us/',views.contact_us, name="contact_us"),
]