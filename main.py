from ImageGenerator import gerar_imagem
from Object import Object
from Cenario import Cenario

vaso = Object('./objetos/coarseTri.botijo.obj')
mesa = Object('./objetos/coarseTri.cube.obj')

mesa.escala(prop_x=20, prop_y=9.75, prop_z=7.7)

vaso.escala(prop_x=0.019, prop_y=0.019, prop_z=0.019)
vaso.rotacao(grau_z=-102)
vaso.translacao(offset_x=22.31, offset_z=4.02, offset_y=4.13)

cenario = Cenario()
cenario.cena = [mesa, vaso]
cenario.setCamera(e=[21, 12, 15], g=[21, 4.625, 3.85], t=[0, 1, 0])
cenario.setProjecao(fov=60, ratio=1, z_near=0, z_far=15)
cenario.translacao(1, 1, 1)
cenario.escala(500, 500)
cenario.transforma_cena()

gerar_imagem(cenario, 1000, 1000)

cenario.salvar_cenario()