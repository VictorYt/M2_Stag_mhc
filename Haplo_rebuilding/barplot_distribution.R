#R code to obtain the distribution profile

#give to R your work directory
mysetwd <- commandArgs(TRUE)
setwd(mysetwd)

#open library
library(ggplot2)
#voir http://www.sthda.com/french/wiki/ggplot2-barplots-guide-de-demarrage-rapide-logiciel-r-et-visualisation-de-donnees pour de jolie barplot


#Read the good input file for each distribution we want
distri <- read.csv2("GvH_distribution", header = TRUE, sep = '\t')
distri_haplo <- read.csv2("HvH_distribution", header = TRUE, sep = '\t')
distri_candidate <- read.csv2("GvcH_distribution", header = TRUE, sep = '\t')


#GvH_distribution
pdf("Distribution_of_mismatch_between_G&H.pdf", height = 10, width = 10)
ggplot(data = distri, aes(x=Number_of_mismatch, y=Number_of_mismatch_occurency)) +
  geom_bar(stat="identity", fill="steelblue",  position=position_dodge()) +
  geom_text(aes(label=Number_of_mismatch_occurency), vjust=1.6, color="black",  position=position_dodge(0.9), size=2) +
  ggtitle("Distribution of mismatch in the comparison between the genotypes and the haplotypes") +
  theme_gray()
#barplot(distri$Number_of_mismatch_occurency, names.arg = distri$Number_of_mismatch ,main = "Distribution des erreurs entre Haplotypes et Genotypes", xlab="nombre d'erreurs", ylab = "occurences de ce nombre d'erreurs")
dev.off()

#HvH_distribution
pdf("Distribution_of_mismatch_between_H&H.pdf", height = 10, width = 10)
ggplot(data = distri_haplo, aes(x=Number_of_mismatch, y=Number_of_mismatch_occurency)) +
  geom_bar(stat = "identity", fill="steelblue") +
  geom_text(aes(label=Number_of_mismatch_occurency), vjust=1.6, color="black", size=2) +
  ggtitle("Distribution of mismatch in the comparison between the the haplotypes") +
  theme_gray()
#barplot(distri_haplo$Number_of_mismatch_occurency, names.arg = distri_haplo$Number_of_mismatch ,main = "Distribution des erreurs entre Haplotypes et Genotypes", xlab="nombre d'erreurs", ylab = "occurences de ce nombre d'erreurs")
dev.off()


#GvcH_distribution
pdf("Distribution_of_mismatch_between_G&cH.pdf", height = 10, width = 10)
ggplot(data = distri_candidate, aes(x=Number_of_mismatch, y=Number_of_mismatch_occurency)) +
  geom_bar(stat="identity", fill="steelblue",  position=position_dodge()) +
  geom_text(aes(label=Number_of_mismatch_occurency), vjust=1.6, color="black",  position=position_dodge(0.9), size=2) +
  ggtitle("Distribution of mismatch in the comparison between the unconfirmed genotypes and the candidates haplotypes") +
  theme_gray()
#barplot(distri$Number_of_mismatch_occurency, names.arg = distri$Number_of_mismatch ,main = "Distribution des erreurs entre Haplotypes et Genotypes", xlab="nombre d'erreurs", ylab = "occurences de ce nombre d'erreurs")
dev.off()
