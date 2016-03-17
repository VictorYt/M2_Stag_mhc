#definition du répertoire de travail
setwd("~/Documents/Stage_victor_Ythier/Analyses/Diversity_of_MHC_and_Haplotype_rebuilding/Haplotypes_Htz/Haplotype_reconstruction/ACP")

#ouverture de la lib ade4
library(ade4)
library(adegenet)
library(Hmisc)#pour fonction impute

#calul le nombre d'occurence dans une table
nmod<-function(x){
  length(table(x))
}

#ACP
#1ère étape : Lecture et manipulation des données
  #avoir des valeurs quantitatives!!!!


#ouverture des inputs
haplo_hmz <- read.csv2("Haplotype_input_format.csv", header = TRUE, sep = "\t")
#add Know: devant le nom des haplo_hmz
haplo_hmz$nom<-as.character(haplo_hmz$nom)
haplo_hmz$nom<-paste("Know:",haplo_hmz$nom, sep='')
haplo_hmz<-as.data.frame(haplo_hmz)
new_haplo <- read.csv2("third_output", header = TRUE, sep = "\t")
new_haplo <- new_haplo[,c(3:82)] 

row.names(haplo_hmz) = haplo_hmz[,1]
haplo_hmz <- haplo_hmz[,2:80]
row.names(new_haplo) = new_haplo[,1]
new_haplo <- new_haplo[,2:80]

  #attention pas un liste unique des nouveaux haplotypes (à récupérer)
all_haplo <- rbind(haplo_hmz, new_haplo)



##quelque info
#Halpo Hmz
haplo_hmz2<-as.vector(as.matrix(haplo_hmz))
table(haplo_hmz2)
#New haplo
new_haplo2<-as.vector(as.matrix(new_haplo))
table(new_haplo2)
#All haplo
all_haplo2<-as.vector(as.matrix(all_haplo))
table(all_haplo2)


##Identifiants
identif<-rownames(all_haplo)
iden<-strsplit(identif, ":")
iden2<-unlist(iden)
#on sépare en 2, l'identification de l'haplotype, comment l'haplotype est obtenu (Know=Hmz, New=script HR sur les Htz)
origin<-iden2[seq(1,length(iden2),2)]
loginName<-iden2[seq(2,length(iden2),2)]


#Les valeurs "--" sont recodées en valeur manquante (NA)
all_haplo<-as.matrix(all_haplo)
all_haplo[all_haplo=="--"]<-NA

all_haplo<-as.data.frame(all_haplo)
  

#Compter les occurences dans le tableau
all_haplo.xnmod<-apply(all_haplo, 2, nmod)
sum(all_haplo.xnmod==0)
sum(all_haplo.xnmod==1)
all_haplo1<-all_haplo[,which(all_haplo.xnmod>1)]
dim(all_haplo1)

#Mise en format "genind" de l'extension adegenet (transformatione en valeur numérique)
all_haplo.genind<-df2genind(all_haplo1, sep = "", pop = origin)

fic<-tab(all_haplo.genind)
dim(fic)
fic1<-fic[,seq(1, ncol(fic),2)]
dim(fic1)
fic1->fic
rm(fic1)
tabmiss<-as.data.frame(1*is.na(fic))
#nombre de valeurs manquantes par colonne:colmiss / ligne:rowmiss
colmiss<-apply(tabmiss, 2, sum)
rowmiss<-apply(tabmiss, 1, sum)
table(colmiss)
table(rowmiss)
dotchart(rowmiss, label="")
dotchart(colmiss, label="")

#Je retire les Markers si plus de 10 individus on des erreurs de calling pour ce marqueur
#Et de la même manière je retir les nouveaux haplotypes qui on plus de 10 markers (12.5%) de marqueurs "--"
anim10<-rowmiss[rowmiss>10]
fic1<- fic[-c(which(rownames(fic) %in% names(anim10))),]
fic2<- fic1[,colmiss<10]
tabmiss=as.data.frame(1* is.na(fic2))
colmiss<-apply(tabmiss, 2, sum)
rowmiss<-apply(tabmiss, 1, sum)
cumsum(unclass(table(colmiss)))

#Remplacement des donneés manquantes restantes par la valeur moyenne de SNP
fic2<-as.data.frame(fic2)
fic2i<-fic2
fic2i[,1:length(fic2)]<-impute(fic2[,1:length(fic2)],what="mean")
fic2i<-fic2i/2
pro<-apply(fic2i, 2, mean) #fréquences totales
std<-sqrt (pro*(1-pro) ) #écart type
xystd<-scale(fic2i, center = TRUE, scale = std) #matrice centré réduite
#identif<-rownames(xystd)
#iden<-strsplit(identif, ":")
#iden<-unlist(iden)
#iden1<-iden[seq(1,length(iden),2)]
#origin<-iden[seq(2,length(iden),2)]
#popg<-factor(origin)
#popg<-factor(origin, exclude = NULL)
#table(popg)


#Analyse en composantes Principales
xy.pca<-dudi.pca(xystd, scale=FALSE, scannf=FALSE, nf = nrow(xystd)-1) #ACP - on retient tous les axes
par(mfrow=c(2,2))
barplot(xy.pca$eig)
s.class(xy.pca$li, fac = as.factor(popg), col = rep(1:5,3),xax = 1, yax = 2)
title(sub = "Axes 1 & 2")
s.class(xy.pca$li, fac = as.factor(popg), col = rep(1:5,3),xax = 1, yax = 3)
title(sub = "Axes 1 & 3")
s.class(xy.pca$li, fac = as.factor(popg), col = rep(1:5,3),xax = 2, yax = 3)
title(sub = "Axes 2 & 3")
mtext("ACP sur haplotype normalisés", outer = TRUE, line = -2)
acpeig<-100*round(xy.pca$eig/sum(xy.pca$eig),2)
par(mfrow=c(1,1))
