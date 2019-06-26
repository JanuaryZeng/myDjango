from django.contrib import admin


from . import models

admin.site.register(models.lovertable)
admin.site.register(models.moneychangetable)
admin.site.register(models.moneytypetable)