from django.urls import path
from . import views
from inbox.views import ListThreads, CreateThread, ThreadView, CreateMessage

urlpatterns = [
path('', ListThreads.as_view(), name='inbox'),
path('create-thread<int:pk>', CreateThread.as_view(), name='create-thread'),
path('delete-thread/<int:pk>', views.deleteThread, name="delete-thread"),
path('<int:pk>', ThreadView.as_view(), name='thread'),
path('<int:pk>/create-message', CreateMessage.as_view(), name='create-message')

]