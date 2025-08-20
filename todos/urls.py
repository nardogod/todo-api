from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'todos', TaskViewSet)  # agora o endpoint é /api/todos/

urlpatterns = router.urls
