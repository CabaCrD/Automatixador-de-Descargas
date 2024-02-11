# Author: CabaCrd
# ES UN ATOMATIZADOR QUE MOVERA AUTOMATICAMENTE LOS ARCHIVOS AUTOMATICAMENTE A SUS CARPETAS DE SISTEMA
# FUNCIONA PARA EL SISTEMA OPERATIVO LINUX EN ESPAÑOL

import os #IMPORTAMOS OS PARA EL MANEJO DE DIRECTORIOS
import getpass #IMPORTAMOS GETPASS PARA OBTENER EL NOMBRE DE USUARIO DE NUESTRA CUENTA


user = getpass.getuser() #OBTENEMOS EL NOMBRE DE USUARIO DE LA CUENTA DESDE LA QUE SE EJECUTA EL SCRIPT

try:
    #LINUX FOLDERS
    CDescargas ="/home/"+user+"/Descargas/" 
    cMusica = "/home/"+user+"/Música/Automatizador/" 
    cImg = "/home/"+user+"/Imágenes/Automatizador/" 
    cVideos ="/home/"+user+"/Vídeos/Automatizador/" 
    cDoc = "/home/"+user+"/Documentos/Automatizador/"
    #AHORA REPASAREMOS EL CONTENIDO DE LA CARPETA DESCARGAS DISCRIMINANDO POR TIPO DE ARCHIVO,
    #CADA TIPO DE ARCHIVOS SERA MOVIDO A SU CORRESPONDIENTE CARPETA
    if __name__ == "__main__":
        for archivo in os.listdir(CDescargas): #BUCLE PARA RECORRER TODO EL DIRECTORIO
            nombre, extension = os.path.splitext(CDescargas + archivo) # PARA CARGA EL NOMBRE DE LA CARPETA Y DEL ARCHIVO
            if extension in [".jpg",".jpeg", ".png", ".gif", ".psd", ".svg", ".bmp"]: #REVISAMOS QUE CUMPLA CON ESTAS CONDICIONES (IMAGEN)
                if not os.path.exists(cImg): #SI NO EXISTE EL DIRECTORIO
                    os.mkdir(cImg) #CREAMOS EL DIRECTORIO
                os.rename(CDescargas + archivo, cImg + archivo) #AQUI MOVEMOS EL ARCHIVO
            if extension in [".avi",".mp4", ".mkv", ".flv", ".mov", ".wmv", ".divx", ".xdiv",".rm"]: #REVISAMOS QUE CUMPLA CON ESTAS CONDICIONES (VIDEO)
                if not os.path.exists(cVideos): #SI NO EXISTE EL DIRECTORIO
                    os.mkdir(cVideos) #CREAMOS EL DIRECTORIO
                os.rename(CDescargas + archivo, cVideos + archivo) #AQUI MOVEMOS EL ARCHIVO
            if extension in [".mp3","ogg",".wav",".au", ".mpeg-4",".aac",".opus",".dsd"]: #REVISAMOS QUE CUMPLA CON ESTAS CONDICIONES (AUDIO)
                if not os.path.exists(cMusica): #SI NO EXISTE EL DIRECTORIO
                    os.mkdir(cMusica) #CREAMOS EL DIRECTORIO
                os.rename(CDescargas + archivo, cMusica + archivo) #AQUI MOVEMOS EL ARCHIVO
            if extension in [".doc",".docx",".dot",".epub",".pdf", ".csv",".odt",".dotx",".ott",".fott"]: #REVISAMOS QUE CUMPLA CON ESTAS CONDICIONES (DOCUMENTOS)
                if not os.path.exists(cDoc): #SI NO EXISTE EL DIRECTORIO
                    os.mkdir(cDoc) #CREAMOS EL DIRECTORIO
                os.rename(CDescargas + archivo, cDoc + archivo) #AQUI MOVEMOS EL ARCHIVO
except:
    print("Ha ocurrido un error inesperado")
