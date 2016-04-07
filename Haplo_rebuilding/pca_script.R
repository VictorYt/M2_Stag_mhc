#R code to obtain the PCA profile

#give to R your work directory
mysetwd <- commandArgs(TRUE)
setwd(mysetwd)

#library you must have for a good run
library(ade4)
library(adegenet)
library(Hmisc)#pour fonction impute


#Function to have occurency number in each table
nmod<-function(x){
  length(table(x))
}


#####
#ACP#
#####
#This PCA is adaptide for our data (no have a unique population and the same number of indiv for each population)


#1st step : Reading and manipulating data
#(have qualitative values)



###Read Inputs###
#Haplotypes we already Know#
haplo_hmz <- read.csv2("Haplotype_input_format.csv", header = TRUE, sep = "\t")
#add Know: devant le nom des haplo_hmz
haplo_hmz$haplo<-as.character(haplo_hmz$haplo)
haplo_hmz$haplo<-paste("Known:",haplo_hmz$haplo, sep='')
haplo_hmz<-as.data.frame(haplo_hmz)
row.names(haplo_hmz) = haplo_hmz[,1]
haplo_hmz <- haplo_hmz[,2:length(haplo_hmz)]

#Candidats Haplotypes#
#(attention not a list of unique haplotype ...)
new_haplo <- read.csv2("run1_candidates_Haplotypes", header = TRUE, sep = "\t")
new_haplo <- new_haplo[,c(3:length(new_haplo))] 
row.names(new_haplo) = new_haplo[,1]
new_haplo <- new_haplo[,2:length(new_haplo)]
  #The "--" values are encoded in missing value (NA)
new_haplo<-as.matrix(new_haplo)
new_haplo[new_haplo=="--"]<-NA
new_haplo<-as.data.frame(new_haplo)

#All haplotypes data#
all_haplo <- rbind(haplo_hmz, new_haplo)


#Some informations (alleles occurency (TOP/BOT strand and A/B allele here))
#Halpo Hmz
haplo_hmz.i<-as.vector(as.matrix(haplo_hmz))
table(haplo_hmz.i)
#New haplo
new_haplo.i<-as.vector(as.matrix(new_haplo))
table(new_haplo.i)
#All haplo
all_haplo.i<-as.vector(as.matrix(all_haplo))
table(all_haplo.i)
#I will see them where? --> look for an output document stdout de subprocess




#2nd step : Data preparation

##IDs
#Haplotypes we already Know#
identif.known<-rownames(haplo_hmz)
iden<-strsplit(identif.known, ":")
iden.known<-unlist(iden)

origin.known<-iden.known[seq(1,length(iden.known),2)]
IDs_name.known<-iden.known[seq(2,length(iden.known),2)]

#Candidats Haplotypes#
identif.new<-rownames(new_haplo)
iden<-strsplit(identif.new, ":")
iden.new<-unlist(iden)

origin.new<-iden.new[seq(1,length(iden.new),2)]
IDs_name.new<-iden.new[seq(2,length(iden.new),2)]

#All haplotypes data#
identif.all<-rownames(all_haplo)
iden<-strsplit(identif.all, ":")
iden.all<-unlist(iden)

origin.all<-iden.all[seq(1,length(iden.all),2)]
IDs_name.all<-iden.all[seq(2,length(iden.all),2)]





#3rd step : Getting Format "genind" extension "adegent"
#Haplotypes we already Know#
haplo_hmz.genind<-df2genind(haplo_hmz, sep = "", pop = factor(origin.known))

#Candidats Haplotypes#
new_haplo.genind<-df2genind(new_haplo, sep = "", pop = factor(origin.new))

#All haplotypes data#
all_haplo.genind<-df2genind(all_haplo, sep = "", pop = factor(origin.all))





#4st step : Missing data (graphics and replacing missing data by the average of the SNP)
#(ici aussi gérer les stdouts)
#(voir pour faire des graphe ggplot2)
#Haplotypes we already Know#
fic<-tab(haplo_hmz.genind)
dim(fic)
fic1<-fic[,seq(1, ncol(fic),2)]
dim(fic1)
fic1->fic
rm(fic1)
tabmiss.known<-as.data.frame(1*is.na(fic))
  #number of missing values per column: colmiss/ row: rowmiss
colmiss.known<-apply(tabmiss.known,2,sum)
rowmiss.known<-apply(tabmiss.known,1,sum)
  #frequency of missing values by SNP
table(colmiss.known)
table(rowmiss.known)
  #graphics
dotchart(colmiss.known, label="")
dotchart(rowmiss.known, label="")



#Candidats Haplotypes#
fic<-tab(new_haplo.genind)
dim(fic)
fic1<-fic[,seq(1, ncol(fic),2)]
dim(fic1)
fic1->fic
rm(fic1)
tabmiss.new<-as.data.frame(1*is.na(fic))
#number of missing values per column: colmiss/ row: rowmiss
colmiss.new<-apply(tabmiss.new,2,sum)
rowmiss.new<-apply(tabmiss.new,1,sum)
#frequency of missing values by SNP
table(colmiss.new)
table(rowmiss.new)
#graphics
dotchart(colmiss.new, label="")
dotchart(rowmiss.new, label="", color = "blue")

#All haplotypes data#
fic<-tab(all_haplo.genind)
dim(fic)
fic1<-fic[,seq(1, ncol(fic),2)]
dim(fic1)
fic1->fic
rm(fic1)
tabmiss.all<-as.data.frame(1*is.na(fic))
#number of missing values per column: colmiss/ row: rowmiss
colmiss.all<-apply(tabmiss.all,2,sum)
rowmiss.all<-apply(tabmiss.all,1,sum)
#frequency of missing values by SNP
table(colmiss.all)
table(rowmiss.all)
#graphics
dotchart(colmiss.all, label="")
dotchart(rowmiss.all, label="")




#Last step : Principal components analysis
#(xystd change 3 fois faire une fonction avec le xystd qui change)
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