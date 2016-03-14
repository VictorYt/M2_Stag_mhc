#definition du répertoire de travail
setwd("~/Documents/Stage_victor_Ythier/Analyses/Diversity_of_MHC_and_Haplotype_rebuilding/Haplotypes_Htz/Haplotype_reconstruction/ACP")

#ouverture de la lib ade4
library(ade4)

#ouverture des inputs
haplo_hmz <- read.csv2("Haplotype_input_format.csv", header = TRUE, sep = "\t")
new_haplo <- read.csv2("third_output", header = TRUE, sep = "\t")
new_haplo <- new_haplo[,c(3:82)] 

row.names(haplo_hmz) = haplo_hmz[,1]
haplo_hmz <- haplo_hmz[,2:80]
row.names(new_haplo) = new_haplo[,1]
new_haplo <- new_haplo[,2:80]

  #attention pas un liste unique des nouveaux haplotypes
all_haplo <- rbind(haplo_hmz, new_haplo)





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




