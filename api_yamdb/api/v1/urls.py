from rest_framework.routers import DefaultRouter
from api.v1.views import (
    CategoryViewSet, CommentViewSet, GenreViewSet,
    ReviewViewSet, TitleViewSet, UserViewSet
)

ENDPOINTS = [
    ('titles', TitleViewSet, 'titles'),
    ('genres', GenreViewSet, 'genres'),
    ('categories', CategoryViewSet, 'categories'),
    (r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, 'reviews'),
    (
        r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
        CommentViewSet,
        'comments'
    ),
    ('users', UserViewSet, 'users'),
    ('users/me', UserViewSet, 'users'),
]

router_v1 = DefaultRouter()

for endpoint, viewset, basename in ENDPOINTS:
    router_v1.register(endpoint, viewset, basename)
