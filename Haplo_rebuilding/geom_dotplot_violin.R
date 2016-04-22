#R code to obtain the violin plot

#give to R your work directory
mysetwd <- commandArgs(TRUE)
setwd(mysetwd)

#open library
library(ggplot2)

#Read the good input file for each distribution we want
occu_dist <- read.csv2("Candidates_Haplotypes_occ", header = TRUE, sep = '\t')
occu_dist$run1_occurency <-as.factor(occu_dist$run1_occurency)


##############
#Geom_dotplot#
##############
#Generate a violin plot of haplotype occurency after the 1st and 2nd run
#générate on continue aes x tu add y=x to select our better candidates
pdf("violin_dotplot_new_Haplotype_occ.pdf", height = 10, width = 10)
ggplot(data = occu_dist, aes(x=run1_occurency, y=run2_redundancy, color=run1_occurency)) +
  geom_violin(trim = TRUE) +
  #geom_dotplot(binaxis='y', stackdir='center', binwidth = 0.1 ) + 
  geom_jitter(shape=16, position = position_jitter(0.2)) +
  #stat_summary(fun.y=mean, geom="point", size=2, color="red") +
  ggtitle("Violin distribution of new Haplotype occurency") +
  xlab("First run occurency") +  ylab ("Second run redundancy")
dev.off()

#################################################
#Missing data and occurency after the second run#
#################################################
#Generate a dotplot of the number between missing allele and 2nd run occurency 
pdf("Missing_data_&_occurency_of_haplotype.pdf", height = 10, width = 10)
ggplot(data = occu_dist, aes(x=run2_redundancy, y=missing_data)) +
  geom_point(aes(colour=missing_data)) +
  ggtitle("Missing data distribution") +
  xlab("Second run occurency") +  ylab ("Number of missing data")
dev.off()
