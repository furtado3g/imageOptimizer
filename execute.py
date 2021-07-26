from src.controller.resizer import optimizeImage
from src.controller.zipGenerator import ZipFolder
import os

path = '{dir}/images'.format(dir=os.getcwd())

optimizeImage(
    path=path,
    basewidth=175,
    type='Geral'
)

ZipFolder(
    path=path
)
