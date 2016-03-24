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
occu_dist$Name <- ifelse(occu_dist$run2_occurency>8 ,  "Occurence > 8", "Not Sig")

ggplot(data = occu_dist, aes(x=missing_data, y=run2_occurency)) +
  geom_point(aes(color=Name)) +
  scale_color_manual(values = c("red", "grey")) +
  theme_bw(base_size = 10) + theme(legend.position = "bottom") +
  geom_text_repel(
    data = subset(occu_dist, run2_occurency > 8),
    aes(label = Name),
    size =5,
    box.padding = unit(0.35, "lines"), 
    point.padding = unit(0.3, "lines")
      )
