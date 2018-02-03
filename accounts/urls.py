from django.urls.conf import re_path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet, EmailViewSet

router = DefaultRouter()
router.register("accounts", AccountViewSet, base_name='accounts')
router.register("emails", EmailViewSet, base_name='emails')

urlpatterns = [
    re_path(r'^', include(router.urls))
]
