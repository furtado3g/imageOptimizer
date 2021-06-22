from PIL import Image
from os import listdir
from os.path import isfile, join


class optimizeImage:
    def __init__(self, path, basewidth):
        self.path = path
        self.basewidth = basewidth
        self.files = [f for f in listdir(path) if isfile(join(path, f))]
        self.execute()

    def resize(self, im):
        wpercent = (self.basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        return im.resize((self.basewidth, hsize), Image.ANTIALIAS)

    def imageManipulator(self, fileName):
        imagePath = self.path+'/'+fileName
        filename = self.path+'/'+fileName[1:fileName.find('.')+1]+'jpg'
        print(fileName)
        im = Image.open(imagePath)
        img = self.resize(im=im)
        imagePath = self.path+'/'+filename
        img.save(self.path+'/'+fileName, 'jpeg')

    def execute(self,):
        for image in self.files:
            self.imageManipulator(image)
