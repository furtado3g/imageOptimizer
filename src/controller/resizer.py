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
        self.carteirinhas = []
        self.db = ExecuteSql()
        self.saveToDb = False

    def setType(self, pTpMatricula):
        self.tpMatricula = pTpMatricula
    
    def setNrAnoSemeste(self, pNrAnoSemeste):
        self.nrAnoSemeste = pNrAnoSemeste

    def resize(self, im):
        wpercent = (self.basewidth/float(im.size[0]))
        hsize = int((float(im.size[1])*float(wpercent)))
        return im.resize((self.basewidth, hsize), Image.ANTIALIAS)

    def imageManipulator(self, fileName):
        imagepath = self.path+'/'+fileName
        filename, fileType = fileName.split('.')
        im = Image.open(imagepath)
        img = self.resize(im=im)
        if self.type != 'Geral':
            for row in self.db.realizarBusca(sqFuncionario=filename):
                if row[0] == 'S':
                    imagepath = self.path+'/'+row[1]+'.jpg'
                    img.save(imagepath, 'jpeg', quality=50, optimize=True)
        else :
            filename = self.db.nomeAtualizado(filename) 
            imagepath = self.path+'/'+filename+'.jpg'
            img.save(imagepath, 'jpeg', quality=50, optimize=True)
        if imagepath != self.path+'/'+fileName :
            imagepath = self.path+'/'+fileName
            remove(imagepath) 

    def execute(self,):
        carteirinhas = []
        resultado = []
        for image in self.files:
            self.imageManipulator(image)
            filename, fileType = image.split('.')
            filename = self.db.nomeAtualizado(filename)
            carteirinhas.append((filename,self.tpMatricula,self.nrAnoSemeste,'I'))
        if self.type == 'Lote' and self.saveToDb == True:
            resultado = self.db.insere_lote(data=carteirinhas)
        return resultado
