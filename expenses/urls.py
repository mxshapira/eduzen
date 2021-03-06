from rest_framework import routers

from .views import CategoryViewSet, ExpenseViewSet

router = routers.DefaultRouter()
router.register(r"expense", ExpenseViewSet)
router.register(r"category", CategoryViewSet)

urlpatterns = []

urlpatterns += router.urls
