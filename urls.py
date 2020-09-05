from django.urls import path
from django.conf.urls import url
from . import views

app_name='bpitool'

urlpatterns = [
    path('', views.index, name='index'),
    path('insane_table', views.insane_table, name='insane_table'),
    path('stella_table', views.stella_table, name='stella_table'),
    path('satellite_table', views.satellite_table, name='satellite_table'),
    path('satellite_score', views.satellite_score, name="satellite_score"),
    path('stella_score', views.stella_score, name="stella_score"),
    path('dpsl_score', views.dpsl_score, name="dpsl_score"),
    path('dpoj_score', views.dpoj_score, name="dpoj_score"),
    path('overjoy_score', views.overjoy_score, name="overjoy_score"),
    path('dpex_score', views.dpex_score, name="dpex_score"),
    path('insane_score', views.insane_score, name="insane_score"),
    path('song_information/<str:table>/<str:song_id>', views.song_information, name="song_information")
]