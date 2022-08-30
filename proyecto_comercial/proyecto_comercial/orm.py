from django.db.models import Q

from proyecto_comercial.wsgi import get_wsgi_application
print("python en django")
from aplicaciones.core.models import Linea, Grupo
# Se presentan todos los atributos si no se especifican los campos
#Insertar registros

#
# Linea.objects.create(descripcion="Mi juguetería")
# # lin = Linea.objects.values('id',"descripcion")
# lin = Linea(descripcion='a').save()
# lin.save()
# print("_"*50)
# linea = Linea.objects.all()
# print(linea)
# print("-"*5)

print("-"*50)
# lin = Linea.objects.get(id=7)
# lin.delete()
# lin.descripcion="HOLA"
# lin.save()
# print(lin.id,lin.descripcion,lin.estado)
# #
# pepo = Linea.objects.values()
# print(pepo)
# print("-"*5)

# print("all(): ",Linea.objects.all())
# print("values(): ",Linea.objects.values())
# print("get(): ",Linea.objects.get(pk=9))
# print("filter(): ",Linea.objects.filter(id=7))
# print("exclude(): ",Linea.objects.exclude(id=7))

# lin = Linea.objects.filter(id=9)
# lin = Linea.objects.filter(id__gt=12)
# lin = Linea.objects.filter(descripcion__icontains="pas")

# lin = Linea.objects.filter(Q(descripcion__istartswith="pas") | Q(id=7))
#
# print(lin.values("id","descripcion"))
#crea el campo con la id
# lin = Linea.objects.get(id=1)
# gru = Grupo.objects.create(descripcion="Gorras",linea__id=1)
# print(gru)
# print(Grupo.objects.values())
