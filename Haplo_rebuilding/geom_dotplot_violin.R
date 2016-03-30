#R code to obtain the violin plot

#give to R your work directory
mysetwd <- commandArgs(TRUE)
setwd(mysetwd)

#open library
library(ggplot2)
#voir http://www.sthda.com/french/wiki/ggplot2-barplots-guide-de-demarrage-rapide-logiciel-r-et-visualisation-de-donnees pour de jolie barplot

#Read the good input file for each distribution we want
occu_dist <- read.csv2("new_Haplotypes_occ", header = TRUE, sep = '\t')
occu_dist$run1_occurency <-as.factor(occu_dist$run1_occurency)

#Geom_dotplot
pdf("violin_dotplot_new_Haplotype_occ.pdf", height = 10, width = 10)
ggplot(data = occu_dist, aes(x=run1_occurency, y=run2_occurency, color=run1_occurency)) +
  geom_violin(trim = FALSE) +
  scale_color_brewer(palette="Accent") +
  #geom_dotplot(binaxis='y', stackdir='center', binwidth = 0.1 ) +
  stat_summary(fun.y=mean, geom="point", size=2, color="red") +
  ggtitle("Violin distribution of new Haplotype occurency")
dev.off()


#Missing data and occurency after the second run
pdf("Missing_data_&_occurency_of_haplotype.pdf", height = 10, width = 10)
ggplot(data = occu_dist, aes(x=run2_occurency, y=missing_data)) +
  geom_point(aes(colour=missing_data)) +
  ggtitle("Missing data distribution")
dev.off()
