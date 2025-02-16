from django.contrib import admin

# Register your models here.

from loja_online.models import Categoria, Produto


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('cid', 'titulo')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'preco', 'product_status')
    list_filter = ('product_status', 'en_estoque')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)