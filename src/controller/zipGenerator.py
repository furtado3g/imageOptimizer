import os
import zipfile
from src.controller.searchStatus import ExecuteSql
from datetime import date


class ZipFolder:
    def __init__(self, path):
        self.path = path
        self.__main()

    def __compress(self):
        today  = date.today()
        zipf = zipfile.ZipFile('temp/{day}{month}{year}.zip'.format(day="{0:0=2d}".format(today.day),month="{0:0=2d}".format(today.month),year=today.year), 'w', zipfile.ZIP_DEFLATED)
        self.__zipdir(self.path, zipf)
        zipf.close()

    def __main(self):
        self.__compress()

    def __zipdir(self,path, ziph):
        lenDirPath = len(path)
        for root, dirs, files in os.walk(path):
            for file in files:
                filePath = os.path.join(root, file)
                ziph.write(filePath , filePath[lenDirPath :])
