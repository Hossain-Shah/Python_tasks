from django.contrib import admin
from .models import urlShortener


class urlShortenerAdmin(admin.ModelAdmin):
    list_display = (
        "longurl",
        "shorturl"
    )
    search_fields = (
        "longurl",
        "shorturl"
    )


admin.site.register(urlShortener, urlShortenerAdmin)

