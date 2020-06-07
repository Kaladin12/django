from django.db import models

# Create your models here.

class base(models.Model):
    theType = models.CharField(max_length =100, blank = False )
    price = models.IntegerField()
    status = models.CharField(max_length=500, blank=True, default = "Disponible")
    disponibles = models.IntegerField()

    choices = (
        ("EXISTENTE", "El articulo se encuentra e existencia"),
        ("AGOTADO", "El articulo está agotado")
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "Type: {0} \nPrice: {1}".format(self.theType, self.price)


class alimentos(base):
    pass

class suplementos(base):
    pass

