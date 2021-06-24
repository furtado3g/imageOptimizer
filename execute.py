from src.controller.resizer import optimizeImage
from src.controller.zipGenerator import ZipFolder

path = 'C:/Users/lfurtado/Desktop/fotos'

optimizeImage(
    path='C:/Users/lfurtado/Desktop/fotos',
    basewidth=175,
    type='Geral'
)

""" ZipFolder(
    path=path
)
 """