from django.contrib import admin
from Series.apps.home.models import Series, Genero, Editorial, Idioma, Figuras, Marca, Manga
from Series.apps.home.models import user_profile


admin.site.register(Series)
admin.site.register(Genero)
admin.site.register(Marca)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Manga)
admin.site.register(Figuras)
admin.site.register(user_profile)