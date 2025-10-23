from django.contrib import admin
from .models import Produto, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)
    

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'categoria', 'codigo_barras')
    search_fields = ('codigo', 'nome', 'categoria', 'codigo_barras')
    list_filter = ('categoria',)
    ordering = ('codigo',)
    
    fieldsets = (
        ('Identificação', {
            'fields': ('codigo', 'codigo_barras')
        }),
        ('Dados do Produto', {
            'fields': ('categoria', 'nome', 'descricao', 'preco')
        }),
    )

    readonly_fields = ('codigo',)  # importante: campo sequencial não deve ser editável
