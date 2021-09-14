from django.contrib import admin
from credits.models import Credit, Client


class CreditAdmin(admin.ModelAdmin):
    list_display = ["id", "client", "created_at", "modified_at", "sbs_debt", "ai_index", "sentinel_index", "status"]


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Credit, CreditAdmin)
admin.site.register(Client, ClientAdmin)
