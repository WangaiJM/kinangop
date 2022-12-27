from django.contrib import admin
from .models import about, board_of_governor, principal, statement,dean

admin.site.register(about)
admin.site.register(statement)
admin.site.register(board_of_governor)
admin.site.register(principal)
admin.site.register(dean)