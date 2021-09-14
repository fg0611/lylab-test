from rest_framework.serializers import ModelSerializer
from credits.models import Credit, Client


class CreditSerializer(ModelSerializer):
    class Meta:
        model = Credit
        fields = ["id", "client", "amount", "sbs_debt", "ai_index", "sentinel_index", "status"]


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "gender", "birthday"]
