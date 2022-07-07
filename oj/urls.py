from django.urls import path,include               
# from .api import QuestionViewSet
# from rest_framework import routers   
from . import views
# from .api import QuestionViewSet 

# router = routers.DefaultRouter()                   
# router.register('', QuestionViewSet, 'questions')  

urlpatterns = [
    # path('', index, name='front'),
    path('problems/', views.getProblems,name=  "problems"),
    path('problems/<str:pk>', views.getProbDetail,name=  "problems-details") 
    # path('problems/',problems,name='problems')
    # path('admin/', admin.site.urls),
]
