import django.urls

import aboniment.views


urlpatterns = [
    django.urls.path('create/', aboniment.views.AbonimentCreateAPIView.as_view(), name='create'),
    django.urls.path('all/', aboniment.views.AbonimentListAPIView.as_view(), name='list'),
    django.urls.path('<int:pk>/', aboniment.views.AbonimentDetailUpdateDeleteAPIView.as_view(), name='concrete'),
]
