from src.controller.resizer import optimizeImage
from src.controller.zipGenerator import ZipFolder
import os

path = '{dir}/images'.format(dir=os.getcwd())

optimizer = optimizeImage(
    path=path,
    basewidth=175,
    type='Geral'
)
optimizer.setNrAnoSemeste('20211')
optimizer.setType('F')
optimizer.execute()

ZipFolder(
    path=path
)
