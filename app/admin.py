from django.contrib import admin
from app.models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'valor', 'quantidade')

admin.site.register(Produto,ProdutoAdmin)
