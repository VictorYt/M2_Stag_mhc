#definition du répertoire de travail
setwd("~/Documents/Stage_victor_Ythier/Analyses/Diversity_of_MHC_and_Haplotype_rebuilding/Haplotypes_Htz/Haplotype_reconstruction/ACP")

#ouverture de la lib ade4
library(ade4)
library(adegenet)

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
#Changement dans le format de données (biallélique)
#Pas besoin finalement pour la fonction df2genind
#all_haplo[all_haplo=="A"]<-"AA"
#all_haplo[all_haplo=="C"]<-"CC"
#all_haplo[all_haplo=="G"]<-"GG"
#all_haplo[all_haplo=="T"]<-"TT"

all_haplo<-as.data.frame(all_haplo)
  

#Compter les occurences dans le tableau
all_haplo.xnmod<-apply(all_haplo, 2, nmod)
sum(all_haplo.xnmod==0)
sum(all_haplo.xnmod==1)
all_haplo1<-all_haplo[,which(all_haplo.xnmod>1)]
dim(all_haplo1)

#Mise en format "genind" de l'extension adegenet (transformatione en valeur numérique)
all_haplo.genind<-df2genind(all_haplo1, sep = "", pop = origin)















##ALL ade4 packages
#ACP
#1ère étape : avoir des valeurs quantitatives!!!!
#2ème étape : virer les valeurs manquante si ce sont des --?
  #aperçu rapide
layout(matrix(c(1:80), 8, 10))
for (i in 1:80) {hist(haplo_hmz[,i], main = names(haplo_hmz) [i], xlab = "")}
layout(1)
  #relations entre les variable quantitatives (ici entre mes marqueurs)
pairs(haplo_hmz, main="Données haplotypes Hmz")

#3ème étape : ACP
  #fontion center et scale de la fonction dudi.pca utilisées pour centrer et réduire les variables (nécessaire pour moi?)
pca_haplo_hmz <- dudi.pca(haplo_hmz, center = T, scale = T, scannf = F)
  #impression des valeurs propres(variantes de chaque composante)
pca_haplo_hmz$eig
  #la vriance cumulées(somme des variances = max?, les données sont centrées réduites)
cumsum(pca_haplo_hmz$eig)
  #les variances en pourcentages et pourcentages cumulés
pca_haplo_hmz$eig/sum(pca_haplo_hmz$eig)*100
cumsum(pca_haplo_hmz$eig/sum(pca_haplo_hmz$eig)*100)
  #histogramme des valeurs propres (représentation en % de variances expliquée)
inertie_haplo_hmz <- pca_haplo_hmz$eig/sum(pca_haplo_hmz$eig)*100
barplot(inertie_haplo_hmz, ylab = "% d'inertie", names.arg = round(inertie_haplo_hmz, 2))
title("Eboulis des valeurs propres en %")
  #interprétation des composantes : les contributions "relatives" (contributuions des variables à la construction des axes)
inertia.dudi(haplo_hmz, col.inertia = T)$col.abs
  #présentation des résultats(plan principal)
#http://www1.montpellier.inra.fr/fp/cdr/ecrire/upload/Racp.pdf (voir p.13)
  #Représentation des résultats (le plan des individus) (voir ggplot2 ici et p.14 du lien ci-dessus)




