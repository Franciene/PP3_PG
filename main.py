from Object import Object
from Cenario import Cenario

vaso = Object('./objetos/coarseTri.botijo.obj')
mesa = Object('./objetos/coarseTri.cube.obj')

mesa.escala(prop_x=20, prop_y=9.75, prop_z=7.7)

vaso.escala(prop_x=0.019, prop_y=0.019, prop_z=0.019)
vaso.rotacao(grau_z=-102)
vaso.translacao(offset_x=22.31, offset_z=4.02, offset_y=4.13)

cenario = Cenario()
cenario.cena = [vaso, mesa]
cenario.setCamera(e=[21, 4.625, 15], g=[21, 4.625, 3.85], t=[0, 1, 0])
cenario.setProjecao(fov=60, ratio=1, z_near=0, z_far=15)
cenario.transforma_cena()
cenario.salvar_cenario()
