from django.contrib import admin
from .models import about, board_of_governor, principal, statement, dean, service_charter, gallery, carousel, dprincipal, registrar, procument, guidance

admin.site.register(board_of_governor)
admin.site.register(principal)
admin.site.register(dprincipal)
admin.site.register(registrar)
admin.site.register(dean)
admin.site.register(procument)
admin.site.register(guidance)
admin.site.register(about)
admin.site.register(statement)
admin.site.register(service_charter)
admin.site.register(gallery)
admin.site.register(carousel)
