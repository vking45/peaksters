from django.contrib import admin
from .models import Match, BetOption, Point, BetEntrie
# Register your models here.
admin.site.register(Match)
admin.site.register(BetOption)
admin.site.register(Point)
admin.site.register(BetEntrie)