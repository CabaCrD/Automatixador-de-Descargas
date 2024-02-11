# Author: CabaCrd
# ES UN ATOMATIZADOR QUE MOVERA AUTOMATICAMENTE LOS ARCHIVOS AUTOMATICAMENTE A SUS CARPETAS DE SISTEMA
# FUNCIONA PARA EL SISTEMA OPERATIVO LINUX EN ESPAÑOL

import os #IMPORTAMOS OS PARA EL MANEJO DE DIRECTORIOS
import getpass #IMPORTAMOS GETPASS PARA OBTENER EL NOMBRE DE USUARIO DE NUESTRA CUENTA
import tkinter #LA PARTE GRAFICA DEL PROGRAMA
import webbrowser # PARA ABIR LA PAGINA DE GITHUN DEL AUTOR

user = getpass.getuser() #OBTENEMOS EL NOMBRE DE USUARIO DE LA CUENTA DESDE LA QUE SE EJECUTA EL SCRIPT

#LA VENTANA QUE SE MOSTRARA CUANDO EJECUTEMOS LA OPERACION
def successWindow():
    window = tkinter.Tk() 
    window.title('Proceso exitoso')
    window.geometry("200x200")
    #ETIQUETA CON EL RESULTADO DEL PROCESO
    label1= tkinter.Label(window, text= "Proceso exitoso. \n Puedes cerrar esta ventana")
    label1.pack()
    #BOTON PARA CERRAR LA VENTANA
    button = tkinter.Button(window, text="Salir", command=window.destroy)
    button.pack()
    #RUN WINDOW
    window.mainloop() 
def fatalWindow():
    #WINDOW WHIT MESSAGE
    window = tkinter.Tk() 
    window.title('Error desconocido')
    window.geometry("200x200")
    #LABEL WHIT WELCOME MESSAGE
    label1= tkinter.Label(window, text= "Error desconocido")
    label1.pack()
    #BUTTON TO OPEN CRYPT MENU 
    button = tkinter.Button(window, text="Salir", command=window.destroy)
    button.pack()
    #RUN WINDOW
    window.mainloop()
def automatizer():
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
                if extension in [".avi",".mp4", ".mkv", ".flv", ".mov", ".wmv", ".divx", "xdiv","rm"]: #REVISAMOS QUE CUMPLA CON ESTAS CONDICIONES (VIDEO)
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
            successWindow()
    except:
        fatalWindow()
def show_GUI(): #START THE GUI OF THE SOFTWARE
    def gitPage():
        webbrowser.open_new("https://github.com/CabaCrD")
    window = tkinter.Tk() 
    window.title('Automatizador')
    window.geometry("400x200")
    #LABEL CON UN MENSAJE DE BIENVENIDA
    label1= tkinter.Label(window, text= "Automatizador\nProyecto creado por CabaCrD")
    label1.pack()
    #BOTON PARA EJECUTAR EL PROGRAMA
    button1 = tkinter.Button(window, text="Mover contenido de la carpeta descargas", command=automatizer)
    button1.pack()
    #BOTON PARA ABRIR LA PAGINA DE GITHUB DEL CREADOR DEL PROGRAMA
    button2 = tkinter.Button(window, text="Página del autor", command=gitPage)
    button2.pack()
    #BOTON PARA CERRAR LA VENTANA
    button3 = tkinter.Button(window, text="Salir del programa", command=window.destroy)
    button3.pack()
    window.mainloop()
show_GUI() #EJECUTAMOS EL PROGRAMA
