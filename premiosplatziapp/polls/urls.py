from django.urls import include, path

from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
# router.register(r'question/<int:pk>', views.question_detail)

urlpatterns = [
    path("", views.index, name="index"),
    # path('questions/', views.question_list),
    # path('questions/<int:pk>', views.question_detail),
    path('', include(router.urls))
]
