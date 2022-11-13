from django.contrib import admin

# Register your models here.
from main.models import Stadium, Match, Team, Ticket, Seat

admin.site.register(Stadium)
admin.site.register(Seat)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Ticket)
