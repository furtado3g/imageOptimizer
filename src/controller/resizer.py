from PIL import Image
from os import listdir, remove
from os.path import isfile, join
from src.controller.searchStatus import ExecuteSql


class optimizeImage:
    def __init__(self, path, basewidth, type):
        self.path = path
        self.basewidth = basewidth
        self.files = [f for f in listdir(path) if isfile(join(path, f))]
        self.type = type
        self.execute()

    def resize(self, im):
        wpercent = (self.basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        return im.resize((self.basewidth, hsize), Image.ANTIALIAS)

    def imageManipulator(self, fileName):
        imagePath = self.path+'/'+fileName
        filename, fileType = fileName.split('.')
        im = Image.open(imagePath)
        img = self.resize(im=im)
        if self.type != 'Geral':
            for row in ExecuteSql().realizarBusca(sqFuncionario=filename):
                if row[0] == 'S':
                    imagePath = self.path+'/'+row[1]+'.jpg'
                    img.save(imagePath, 'jpeg', quality=50, optimize=True)
        else :
            imagePath = self.path+'/'+filename+'.jpg'
            img.save(imagePath, 'jpeg', quality=50, optimize=True)
        
        if imagepath != self.path+'/'+fileName :
            imagePath = self.path+'/'+fileName
            remove(imagePath) 


    def execute(self,):
        for image in self.files:
            self.imageManipulator(image)
