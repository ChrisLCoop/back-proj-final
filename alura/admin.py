from django.contrib import admin

# Register your models here.

from .models import(
    Categoria,Area,Curso,CursoImagen,Pedido,PedidoDetalle
)

admin.site.register(Categoria)
admin.site.register(Area)
#admin.site.register(Curso)
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('sku','curso','categoria','area','precio','dificultad','profesor','idioma')
    list_filter = ('categoria','area')

from django.utils.html import format_html

#admin.site.register(CursoImagen)
@admin.register(CursoImagen)
class CursoImagenAdmin(admin.ModelAdmin):

    def imagen_html(self,obj):
        return format_html('<img src="{}" width=150px />'.format(obj.imagen.url))

    imagen_html.short_description = 'Portada'

    list_display = ('orden','curso','imagen_html')
    search_fields = ['curso__curso']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente_id','id','fecha_registro','nro_pedido','monto_total','estado')

@admin.register(PedidoDetalle)
class PedidoDetalleAdmin(admin.ModelAdmin):
    list_display = ('pedido','producto','cantidad','subtotal','pedido_id')