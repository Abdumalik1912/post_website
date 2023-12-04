from django.urls import path
from .views import homepage, post
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", homepage, name="homepage"),
    path("post/<int:pk>", post, name="post_page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
