from django.contrib import admin

# Register your models here.
from apps.flowers.models import Flowers


class FlowersAdmin(admin.ModelAdmin):
    fields = ('name', )


admin.site.register(Flowers, FlowersAdmin)