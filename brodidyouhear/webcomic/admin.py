from django.contrib import admin
from webcomic.models import Comic

class ComicAdmin(admin.ModelAdmin):
	pass


admin.site.register(Comic, ComicAdmin)