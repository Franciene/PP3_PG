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
cenario.setCamera(e=[30.293, 15.7, 13.534], g=[20, 7.788, -2.333], t=[0, 1, 0])
cenario.transforma_cena()
cenario.salvar_cenario()
