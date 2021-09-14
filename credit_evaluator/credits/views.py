from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from credits.models import Credit, Client
from credits.serializers import CreditSerializer, ClientSerializer 

class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CreditsListCreateAPIView(ListCreateAPIView):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class CreditsListCreateAPIView(ListCreateAPIView):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer


class CreditRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer    

class CreditApproveAPIView(UpdateAPIView):
    queryset = Credit.objects.filter(status="CREATED")
    serializer_class = CreditSerializer

    def update(self, request, *args, **kwargs):
        obj = self.queryset.filter(pk=kwargs["pk"]).first()
        obj.status = "APPROVED"
        obj.save()
        return Response({"message": "Credit approved", "id": kwargs["pk"]})


class CreditDenyAPIView(UpdateAPIView):
    queryset = Credit.objects.filter(status="CREATED")
    serializer_class = CreditSerializer

    def update(self, request, *args, **kwargs):
        obj = self.queryset.filter(pk=kwargs["pk"]).first()
        obj.status = "DENIED"
        obj.save()
        return Response({"message": "Credit denied", "id": kwargs["pk"]})

