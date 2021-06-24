import os
import zipfile
from src.controller.searchStatus import ExecuteSql
from datetime import date


class ZipFolder:
    def __init__(self, path):
        self.path = path
        self.__main()

    def __compress(self):
        zipf = zipfile.ZipFile('temp/fotos.zip', 'w', zipfile.ZIP_DEFLATED)
        self.__zipdir(self.path, zipf)
        zipf.close()

    def __main(self):
        self.__compress()

    def __zipdir(self,path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))
