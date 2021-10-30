from tkinter import *
from tkinter.filedialog import askopenfilename # permet de parcourir les fichiers de notre ordinateur et chosir une image
from tkinter.messagebox import showerror, showinfo # pour afficher des fenetres d'erreur et d'info

class Personnage():
    def __init__(self,prenom,nom,photo):
        self.prenom=prenom
        self.nom = nom
        self.photo = photo

    def __eq__(self, other):
        return (self.prenom == other.prenom and self.nom == other.nom)

def parcourir():
    global imageName
#initialdir="/" cad quand je clique
#title = 'selectionner une image' c'est le titre de la fenetre qui va etre affiché
#filetypes=(("png files","*.png"),("jpeg files","*.jpg")) cad le typede l'image qui va doit etre selectionné soit jpeg ou png
    imn=askopenfilename(initialdir="/", title='selectionner une image',
                        filetypes=(("png files","*.png"),("jpeg files","*.jpg")))
    if imn: #if imn existe
        imageName=imn
    if imageName: #imageName va contenu le chemin de l'image selectionné et le chemin contien des /
        text=imageName.split("/")# mettre dans un tableaules element de ce chemin
        canvasentry.config(text=".../"+text[-1])# le chemin de l'image qui va etre affiché dans la fenetre
        #il va etre affiché sous forme exp:.../homme.png
        #donc .../+le dernier element de la liste et pas tout le chemin

def appartient(liste,val):# permet de tester si une personne a eté dejà ajouté ou pas
    #val represente la personne à verifier
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return 1
    return 0

def valider():#permet de valider les champs
    global listePersonne,imageNames # nous avons importé globalement la variable imageNames
    photo=imageNames
    if entryprenom.get() and entrynom.get() and photo: # si c'est 3 champs ne sont pas vides
        pn= Personnage(entryprenom.get(),entrynom.get(),photo)
        if appartient(listePersonne,pn):
            showerror(title='formulaire invalide',message='cet utilisateur existe dejà!!!!')
        else:
            listePersonne.append(pn)
            showinfo(title='validation reussie',message='{} a eté bien ajouté'.format(entryprenom.get()))
    else:
        showerror(title='formulaire invalide',message='toutes les champs doivent etre renseignés!!!!')

def reinitialiser():# supprimer tous ce qui eté renseigné dans les 3 champs
    global imageName
    entryprenom.delete(0,END)
    entrynom.delete(0, END)
    imageName=''
    canvasentry.config(text="aucune image selectionnée")

# initialisation des variables
imageNames, listePersonne ='',[]


fen=Tk()
frame=Frame(fen,bg="#FD6C9E")#,width="1000",height="1000"
fen.config(bg="#FD6C9E")
fen.title("mon application")
fen.iconbitmap("images/logo-inscription.ico")
fen.geometry("800x450")#attention  c'est le signe fois pas celle du clavier coté chiffre  ×
labelnom=Label(frame,text='votre nom',bg="#FD6C9E")
labelprenom=Label(frame,text='votre prenom',bg="#FD6C9E")
labelphoto=Label(frame,text='votre photo',bg="#FD6C9E")
canvas=Canvas(frame,bg="#1E7FCB")
entrynom=Entry(frame)
entryprenom=Entry(frame)
canvasentry=Label(canvas,text="aucune photo selectionnée",font= 'arial 8 bold', fg='black',bg="#FEBFD2")
validation= Label (frame, text='Entrez vos information ici ', font= 'arial 10 bold', fg='#FD6C9E',bg='white')
b1=Button(frame,text="parcourir",command=parcourir)
b2=Button(frame,text="valider",command=valider)
b3=Button(frame,text="reinitialiser",command=reinitialiser)
b4=Button(frame,text="afficher la liste",command="")
frame.pack()
validation.grid(row=1,column=1)
#validation.grid(row=1,column=0)
labelnom.grid(row=2,column=0)
labelprenom.grid(row=3,column=0)
labelphoto.grid()
canvas.grid(row=4,column=1)
entrynom.grid(row=2,column=1)
entryprenom.grid(row=3,column=1)
canvasentry.grid(row=4,column=2)
b1.grid(row=4,column=4)
b2.grid(row=7,column=1)
b3.grid(row=12,column=1)
b4.grid(row=15,column=1)
fen.mainloop()
