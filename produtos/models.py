from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name="Nome da Categoria")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']

class Produto(models.Model):
    codigo = models.CharField(
        max_length=10,
        unique=True,
        editable=False,
        verbose_name="Código do Produto"
    )
    codigo_barras = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name =  "Código de Barras"
    )
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Categoria"
    )

    def save(self, *args, **kwargs):
        # Gera código sequencial se ainda não existir
        if not self.codigo:
            ultimo_produto = Produto.objects.order_by('-id').first()
            if ultimo_produto:
                ultimo_codigo = int(ultimo_produto.codigo)
                novo_codigo = f"{ultimo_codigo + 1:03d}"  # Exemplo: 001, 002...
            else:
                novo_codigo = "001"
            self.codigo = novo_codigo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.nome}" 
   
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']
