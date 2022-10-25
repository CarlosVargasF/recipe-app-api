"""
URL mappings for the recipe app
"""
from django.urls import (
    path,
    include,
)

# create automatically routes for all options of the view
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
