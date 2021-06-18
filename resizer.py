from PIL import Image
from os import listdir
from os.path import isfile, join

class optimizeImage:
    def __init__(self,path):
        self.path = path
        self.files = [f for f in listdir(path) if isfile(join(path, f))]
        self.execute()
    
    def resize(self,im):
        basewidth = 150
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        return im.resize((basewidth,hsize), Image.ANTIALIAS)

    def imageManipulator(self,fileDir):
        im = Image.open(fileDir)
        img = self.resize(im=im)
        img.save(fileDir)
    
    def execute(self,):
        for image in self.files:
            self.imageManipulator(self.path+image)
