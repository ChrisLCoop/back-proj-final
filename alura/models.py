from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_categoria'

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_area'

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.RESTRICT)
    area = models.ForeignKey(Area,on_delete=models.RESTRICT)
    curso = models.CharField(max_length=255,null=True)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=6,decimal_places=2)
    fecha_inicio = models.DateField(null=False)
    popularidad =models.DecimalField(max_digits=4,decimal_places=2)
    profesor = models.CharField(max_length=150,null=True)
    fecha_lanzamiento = models.DateField(null=False)
    idioma = models.CharField(max_length=25,null=True)
    subtitulo = models.CharField(max_length=25,null=True)
    dificultad = models.CharField(max_length=50,null=True)
    duracion = models.CharField(max_length=4,null=True)
    estudiantes = models.CharField(max_length=6,null=True)
    sku = models.CharField(max_length=10,null=True,unique=True)
    nota_a =models.CharField(max_length=200,null=True)
    nota_b =models.CharField(max_length=200,null=True)
    nota_c =models.CharField(max_length=200,null=True)
    nota_d =models.CharField(max_length=200,null=True)
    nota_e =models.CharField(max_length=200,null=True)
    nota_f =models.CharField(max_length=200,null=True)
    nota_g =models.CharField(max_length=200,null=True)
    nota_h =models.CharField(max_length=200,null=True)
    nota_i =models.CharField(max_length=200,null=True)
    nota_j =models.CharField(max_length=200,null=True)
    inclu_a =models.CharField(max_length=200,null=True)
    inclu_b =models.CharField(max_length=200,null=True)
    inclu_c =models.CharField(max_length=200,null=True)
    inclu_d =models.CharField(max_length=200,null=True)
    inclu_e =models.CharField(max_length=200,null=True)
    inclu_f =models.CharField(max_length=200,null=True)
    seccion_conten_titulo_a =models.CharField(max_length=100,null=True)
    seccion_a_detalle_a =models.CharField(max_length=100,null=True)
    seccion_a_detalle_b =models.CharField(max_length=100,null=True)
    seccion_a_detalle_c =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_b =models.CharField(max_length=100,null=True)
    seccion_b_detalle_a =models.CharField(max_length=100,null=True)
    seccion_b_detalle_b =models.CharField(max_length=100,null=True)
    seccion_b_detalle_c =models.CharField(max_length=100,null=True)
    seccion_b_detalle_d =models.CharField(max_length=100,null=True)
    seccion_b_detalle_e =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_c =models.CharField(max_length=100,null=True)
    seccion_c_detalle_a =models.CharField(max_length=100,null=True)
    seccion_c_detalle_b =models.CharField(max_length=100,null=True)
    seccion_c_detalle_c =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_d =models.CharField(max_length=100,null=True)
    seccion_d_detalle_a =models.CharField(max_length=100,null=True)
    seccion_d_detalle_b =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_e =models.CharField(max_length=100,null=True)
    seccion_e_detalle_a =models.CharField(max_length=100,null=True)
    seccion_e_detalle_b =models.CharField(max_length=100,null=True)
    seccion_e_detalle_c =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_f =models.CharField(max_length=100,null=True)
    seccion_f_detalle_a =models.CharField(max_length=100,null=True)
    seccion_f_detalle_b =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_g =models.CharField(max_length=100,null=True)
    seccion_g_detalle_a =models.CharField(max_length=100,null=True)
    seccion_g_detalle_b =models.CharField(max_length=100,null=True)
    seccion_g_detalle_c =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_h =models.CharField(max_length=100,null=True)
    seccion_h_detalle_a =models.CharField(max_length=100,null=True)
    seccion_h_detalle_b =models.CharField(max_length=100,null=True)
    seccion_h_detalle_c =models.CharField(max_length=100,null=True)
    seccion_h_detalle_d =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_i =models.CharField(max_length=100,null=True)
    seccion_i_detalle_a =models.CharField(max_length=100,null=True)
    seccion_i_detalle_b =models.CharField(max_length=100,null=True)
    seccion_i_detalle_c =models.CharField(max_length=100,null=True)
    seccion_i_detalle_d =models.CharField(max_length=100,null=True)
    seccion_conten_titulo_j =models.CharField(max_length=100,null=True)
    seccion_j_detalle_a =models.CharField(max_length=100,null=True)


    class Meta:
        db_table = 'tbl_curso'

    def __str__(self):
        return self.curso

@receiver(post_save,sender=Curso)
def generar_sku(sender,instance,created,**kwargs):
    if created:
        categoria_cod = instance.categoria.nombre[:2].upper()
        correlativo = str(Curso.objects.count()).zfill(3)
        instance.sku = f'{categoria_cod}{correlativo}'
        instance.save()

class CursoImagen(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.RESTRICT)
    imagen = models.ImageField(upload_to='galeria',blank=True)
    orden = models.IntegerField(default=1)
    fecha_registro = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_curso_imagen'
        verbose_name_plural = 'Imagenes del Curso'

    def __str__(self):
        return str(self.imagen)
##modelos para usuarion###
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    nombre = models.CharField(max_length=255)
    dni= models.CharField(max_length=8)
    sexo = models.CharField(max_length=1)
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True)
    direccion = models.TextField()

    class Meta:
        db_table = 'tbl_cliente'

    def __str__(self):
        return self.nombre

##modelos pedido

class Pedido(models.Model):

    ESTADO_CHOICES=(
        ('0','Solicitado'),
        ('1','Pagado')
    )

    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    fecha_registro = models.DateTimeField(auto_now=True)
    nro_pedido = models.CharField(max_length=20,null=True)
    monto_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado = models.CharField(max_length=1,default='0',choices=ESTADO_CHOICES)

    class Meta:
        db_table = 'tbl_pedido'

    def __str__(self):
        return self.nro_pedido

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)
    producto = models.ForeignKey(Curso,on_delete=models.RESTRICT)
    cantidad = models.IntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table = 'tbl_pedido_detalle'

    def __str__(self):
        return self.producto.curso
    
#comentario

class Comentario(models.Model):
    content = models.TextField(max_length=1000, help_text='ingrese un comentario')
    fecha_comentario = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        ordering = ['fecha_comentario']
    
    def __str__(self):
        tamaño_titulo = 20
        if len(self.content) > tamaño_titulo:
            return self.content[:tamaño_titulo] + '...'
        return self.content 
