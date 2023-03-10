from django.urls import include, path

from api.v1.urls import router_v1
from api.v1.views import SignupViewSet, TokenViewSet

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', SignupViewSet.as_view()),
    path('v1/auth/token/', TokenViewSet.as_view()),
]
