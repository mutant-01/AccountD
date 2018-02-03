from rest_framework import viewsets
from accounts.models import Account, Email
from accounts.serializers import AccountSerializer, EmailSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        # todo create/update resource with user or without?
        if self.request.user.is_anonymous:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

    def perform_create(self, serializer):
        # todo create/update resource with user or without?
        if self.request.user.is_anonymous:
            serializer.save()
        else:
            serializer.save(owner=self.request.user)
