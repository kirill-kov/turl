from django.urls import path

from turl_api.views import TurlAPIView

app_name = "turl_api"

urlpatterns = [
    path('new_turl/', TurlAPIView.as_view()),
    path('new_turl/<int:pk>', TurlAPIView.as_view())
]
