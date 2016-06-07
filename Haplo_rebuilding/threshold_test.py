#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (--ih <haplo_file>) (--ig <geno_file>)
    __main__.py (--ih <haplo_file>) (--ig <geno_file>) [-o <filename>] [-t <nb>] [-d] [-f <fP_file>]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    --ih <haplo_file>                       Haplotype input file
    --ig <geno_file>                        Genotype input file
    -o <filename>, --output <filename>      Specifying output file prefix
                                            [default: Output_data]
    -t <nb>, --threshold <nb>               Threshold of accepted errors during haplotype and genotype comparaison 
                                            [default: 0]
    -d, --dist                              Produce distribution graphics based on inputs and outputs files. 
                                            [default: False]
    -f <fP_file>, --fastPHASE <fP_file>     Compare your result by fastPHASE one

"""

if __name__ == "__main__":
    from docopt import docopt
    import os
    import time
    import itertools as it
    #from Object import ClassName, function ...
    from Haplotype import Haplotype
    from Genotype import Genotype
    from used_function import *
    #import used_function as usf
 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Haplotype rebuilding 0.3')
    print (arguments)

    haplotype_file = arguments["--ih"]
    genootype_file = arguments["--ig"]
    output = arguments["--output"]
    threshold = arguments["--threshold"]
    distribution = arguments["--dist"]
    fPcompare = arguments["--fastPHASE"]

    
    #    {'--help': False,
    #     '--input_haplotype':file,
    #     '--input_genotype':file,
    #     '--output': "Output_data",
    #     '--threshold': 0,
    #     '--dist': False,
    #     '--pca': False,
    #     '--cytoscape : False'
    #     '--version': False}


    #http://sametmax.com/path-py-plus-en-detail/








                                            ####################################################
                                            ################### MAIN RUN SCRIPT ################
                                            ####################################################



    if threshold != '0' :
        print ("\nYou use the threshold option")



    dirname = output

    try:
        os.makedirs(dirname)
    except OSError:
        if os.path.exists(dirname):
            # We are nearly safe
            pass
        else:
            # There was an error on creation, so make sure we know about it
            raise

    #############
    ##FIRST RUN##
    #############
    run1_start = time.time()
    print ("\nFirst run start")

    """Construction of the list of Haplotype object"""
    lst_of_haplo_object = read_input_file(haplotype_file, Haplotype, "\t")
    #print ("Haplotype number :",len(lst_of_haplo_object))
    """Construction of my list of Genotype object"""
    lst_of_geno_object = read_input_file(genootype_file, Genotype, "\t")
    #print ("Genotype number :",len(lst_of_geno_object))

    """For each genotype, recovering the number of markers: Hmz, Htz and index them"""
    #print ("Markers are {}:".format(lst_of_geno_object[1].markers))
    for geno in lst_of_geno_object :
        geno.index_htz_markers_in_seq = (geno.position_htz_markers())
        geno.nb_htz_markers = geno.have_nb_htz_markers()
        geno.nb_hmz_markers = geno.have_nb_hmz_markers()
        #print ("There is {} Hmz and {} Htz markers".format(geno.nb_hmz_markers, geno.nb_htz_markers))




# !!!!!!!!!!!!!!!!!!!!!!!!!!!
    #Necessary to write the first output
    #Care of this step if we choise a threshold

    #Pour chaqu'une de mes instances (haplo, geno) je créé le dictionnaire adapté en fonction du seuil
    for geno in lst_of_geno_object :
        geno.half_similarity_with = geno.similar_with_size(threshold)
    for haplo in lst_of_haplo_object :
        haplo.half_similarity_with = haplo.similar_with_size(threshold)
    #pour chaque combinaision je rempli le dictionnaire à la clef correspondante
    for geno, haplo in it.product(lst_of_geno_object, lst_of_haplo_object):
        geno.select_similar_with(haplo, threshold)
    for haplo, geno in it.product(lst_of_haplo_object, lst_of_geno_object) :
        haplo.select_similar_with(geno, threshold)


#    # Look at threshold argument
#    if (threshold != 0):
#        print ("-t used")
#        print (threshold)
#        #blabla 
#    else :
#        print ("-t no used")
#        arguments["-t"] = 0
#   #Ne sera peut être incorporé au code car apparterait trop de faux positif
# !!!!!!!!!!!!!!!!!!!!!!!!!!!
   




    """After finding similar haplotypes to our genotypes, 
    we combine these haplotypes to see if they explain our genotype."""
    #New Haplotype creation and store in lst_of_haplo_object_expanded

    for geno in lst_of_geno_object :
        #What haplotypes combined with another give us our genotype
        geno.probable_haplotypes_combinaison = geno.combinaison_between_similar_haplotype_in_geno_test()
        geno.number_of_probable_haplotypes_combinaison = len(geno.probable_haplotypes_combinaison)
        #New Haplotype creation, store in the genotype attribut : lst_of_new_haplotype
        #geno.lst_of_new_haplotype = geno.have_new_haplotype_test()
        geno.lst_of_new_haplotype = geno.have_new_haplotype_test_better() 
        geno.number_of_new_created_haplotype = len(geno.lst_of_new_haplotype)


    #Here the list of candidates Haplotypes objects
    #lst_of_haplo_object_expanded = new_haplotype_test(lst_of_geno_object) #remplacer par une autre pethode
    lst_of_haplo_object_expanded = new_haplotype_test_extend(lst_of_geno_object) #remplacer par celle-ci
    #change the origine of this candidate haplotype
    for candidate_haplotype in lst_of_haplo_object_expanded :
        candidate_haplotype.origin = "candidate"


    """Reduction of the Genotype list"""
    lst_confirmed_genotype = []
    lst_unconfirmed_genotype = []
    #Are removed genotypes with at least one combination of haplotype
    nb_new_h = 0
    for geno in lst_of_geno_object :
        nb_new_h += geno.number_of_new_created_haplotype
        if geno.number_of_new_created_haplotype == 0 and len(geno.half_similarity_with[0]) > 1 : 
            lst_confirmed_genotype.append(geno)
        else : 
            lst_unconfirmed_genotype.append(geno)
        
    print ("Number of Genotype that can be explained by our Known Haplotypes starting list : {}".format(len(lst_confirmed_genotype)))
    print ("It remains {} unconfirmed Genotypes".format(len(lst_unconfirmed_genotype)))
    print ("Number of candidate Haplotype created : {}".format(nb_new_h))


    """Screening of identical candidates Haplotypes"""
    for new_haplo in lst_of_haplo_object_expanded :
        new_haplo.similar_new_haplotype = new_haplo.screening_himself_test(lst_of_haplo_object_expanded)
        new_haplo.number_of_similar_new_haplotype = len(new_haplo.similar_new_haplotype)
    
    lst_of_haplo_object_expanded_filter = []
    for haplo in lst_of_haplo_object_expanded:
        if haplo.number_of_similar_new_haplotype == 0:
            lst_of_haplo_object_expanded_filter.append(haplo)
        if haplo.number_of_similar_new_haplotype > 0:
            count = 0
            for identiq_haplo in haplo.similar_new_haplotype:
                if identiq_haplo in lst_of_haplo_object_expanded_filter:
                    count += 1
            if count == 0 :
                lst_of_haplo_object_expanded_filter.append(haplo)
    print("Number of candidate Haplotype after screening of redondant : {}".format(len(lst_of_haplo_object_expanded_filter)))



    run1_end = time.time()
    time1 = run1_end - run1_start
    print("1st run is over. \nIt lasted {} sec".format(time1))





    ##############
    ##SECOND RUN##
    ##############
    run2_start = time.time()
    print ("\nSecond run start")

    #Creation of the rigth dictionnary
    for candidate_haplo in lst_of_haplo_object_expanded_filter :
        candidate_haplo.half_similarity_with = candidate_haplo.similar_with_size(threshold)
    #Find the half simmilarity with all the génotype or only the uncorfirmed
    for candidate_haplo, geno in it.product(lst_of_haplo_object_expanded_filter, lst_unconfirmed_genotype) :
        candidate_haplo.select_similar_with(geno, threshold)

    """Count of missing data in Haplotypes sequences"""
    #Here we make a list of all Haplotypes objects
    lst_of_haplo_object_all = lst_of_haplo_object + lst_of_haplo_object_expanded
    #Add to Haplotypes objets missing_data occurence in there sequence
    for haplo in lst_of_haplo_object_all :
        haplo.missing_data_counter()

    """Again we selected the half similar Haplotype to our unconfirmed Genotypes.
    But this time we only takes Haplotypes without mismatch"""
    #Add candidates Haplotypes which are similar to our genotype no confirmed, in the dictionary attribut of half_similary_with
    for geno_non_confirmed, candidates_haplo in it.product(lst_unconfirmed_genotype, lst_of_haplo_object_expanded_filter):
        geno_non_confirmed.select_similar_with(candidates_haplo, 0)
        #geno_non_confirmed.number_of_similar_haplotype = len(geno_non_confirmed.similar_haplotype) #plus besoin de compter la taille de cette liste car devenu un dictionnaire (et pas d'interet)

    """Again we combine Haplotypes (Known and candidate this time) to see if they explain unconfirmed genotype"""
    for geno in lst_of_geno_object :
        #What haplotypes combined with another give us our genotype
        geno.probable_haplotypes_combinaison_2_run = geno.combinaison_between_similar_haplotype_in_geno_test()
        geno.number_of_probable_haplotypes_combinaison_2_run = len(geno.probable_haplotypes_combinaison_2_run)


    """Reduction of the unconfirmed Genotype list"""
    lst_genotype_confirmed_2 = []
    lst_unconfirmed_genotype_2 = []
    #Are removed genotypes with at least one combination of haplotype
    for geno in lst_unconfirmed_genotype :
        if geno.number_of_probable_haplotypes_combinaison_2_run > 0 and len(geno.half_similarity_with[0]) > 1 :
            lst_genotype_confirmed_2.append(geno)
        else : 
            lst_unconfirmed_genotype_2.append(geno)
    print ("Number of Genotype that can be explained by our Known and Candidates Haplotypes list : {}".format(len(lst_genotype_confirmed_2)))
    print ("It remains {} unconfirmed Genotypes".format(len(lst_unconfirmed_genotype_2)))


    run2_end = time.time()
    time2 = run2_end - run2_start
    print("2nd run is over. It lasted {} sec".format(time2))





    ##############
    ##OUTPUT RUN##
    ##############
    run3_start = time.time()
    print("\nAchivement of outputs")
    
    ###RUN 1###
    print("First run outputs")
    """Comparison of each genotype with each Hmz haplotype """
    compare_output(os.path.join(output, "run1_GvH"), lst_of_geno_object, lst_of_haplo_object)
    """A file to see the candidates Haplotypes created"""
    new_haplotype_output(os.path.join(output, "run1_candidates_Haplotypes"), lst_of_geno_object)# a indiquer combien de corerction il y a eut pour chaque Haplotype

    ###RUN 2###
    print("Second run outputs")
    """Comparison of each unconfirmed genotype with each Candidate haplotype """
    compare_output(os.path.join(output, "run2_GvH"), lst_unconfirmed_genotype, lst_of_haplo_object_expanded_filter)
    """A file to see each half similarity (Known & Candidates Haplotypes) with our Genotypes"""
    compare_output_result_test(os.path.join(output, "Compatible_Haplotypes"), lst_of_geno_object)

    ###SUMMARY OUTPUT###
    #create the fonction and put it here



    run3_end = time.time()
    time3 = run3_end - run3_start
    print("Output_given")
    print("it's spend {}".format(time3))






                                            ####################################################
                                            ################# DISTRIBUTION OPTION ##############
                                            ####################################################


    # Look at distribution argument
    if (distribution == True):
        print ("\nDistribution flag used")

        dist = os.path.join(dirname, "Distribution")

        try:
            os.makedirs(dist)
        except OSError:
            if os.path.exists(dist):
            # We are nearly safe
                pass
            else:
            # There was an error on creation, so make sure we know about it
                raise

    ##############
    ##OUTPUT RUN##
    ##############
        run4_start = time.time()

        """The distribution of the run1_GvkH"""
        mismatch_distribution_output(os.path.join(dist,"GvH_distribution"), mismatch_distribution(lst_of_haplo_object, os.path.join(output,"run1_GvH")))

        """The repartition of the mismatch between Genotype and haplotype"""
        #comme le précédent lecture de GvH distribution et écriture du fichier (sommes des colones pour chaques marqueurs)
        
        """The distribution of the run1_kHvkH"""
        compare_output(os.path.join(dist, "run1_HvH"), lst_of_haplo_object, lst_of_haplo_object)
        mismatch_distribution_output(os.path.join(dist, "HvH_distribution"), mismatch_distribution(lst_of_haplo_object_expanded_filter, os.path.join(dist,"run1_HvH")))

        """The distribution of the run2_GvcH"""
        compare_output(os.path.join(dist, "run2_GvcH"), lst_unconfirmed_genotype, lst_of_haplo_object_expanded)
        mismatch_distribution_output(os.path.join(dist,"GvcH_distribution"), mismatch_distribution(lst_of_haplo_object_expanded_filter, os.path.join(dist, "run2_GvcH")))

        """Distribution of the occurence of haplotype hmz during the first run"""
        for haplo in lst_of_haplo_object :
            haplo.similar_occurence = haplo.similarity_time_with()
            haplo.frequency= haplo.similarity_frequency(len(lst_of_geno_object))
        haplotype_redundancy(os.path.join(dist, "Known_Haplotypes_redundancy"), lst_of_haplo_object)
        for candidate_haplo in lst_of_haplo_object_expanded_filter :
            candidate_haplo.similar_occurence = candidate_haplo.similarity_time_with()
            candidate_haplo.frequency= candidate_haplo.similarity_frequency(len(lst_unconfirmed_genotype))
        haplotype_redundancy(os.path.join(dist, "Candidates_Haplotypes_redundancy"), lst_of_haplo_object_expanded_filter)

        """Distribution of the occurrence of new haplotypes during the second run"""
        new_haplotype_occurency(os.path.join(dist, "Candidates_Haplotypes_occ"), lst_of_haplo_object_expanded_filter, lst_unconfirmed_genotype)

        print ("Distribution output files realized") 

    #############
    ##GRAPHIQUE##
    #############
        #And now the functions using subprocess to collect distribution pdf
        run_R_file("barplot_distribution.R", dist)
        #The violin dotplot & occurency of missing data
        run_R_file("geom_dotplot_violin.R", dist)

        print ("Graphique's output realized")

        run4_end = time.time()
        time4 = run4_end - run4_start
        print("it's spend {}".format(time4))





                                            ####################################################
                                            ############## fastPHASE COMPARE OPTION ############
                                            ####################################################




    # Compare with fastPhase résult
    if (fPcompare != None):
        print ("\nCompare your Haplotypes vs fastPHASE Haplotypes")

        fastPHASE_dir = os.path.join(dirname, "fastPHASE_compare")

        try:
            os.makedirs(fastPHASE_dir)
        except OSError:
            if os.path.exists(fastPHASE_dir):
            # We are nearly safe
                pass
            else:
            # There was an error on creation, so make sure we know about it
                raise

        #print("You chose to compare our result by the fastPHASE result for the same data")
        run5_start = time.time()


        """Construction of the list of Haplotype object (fastPHASE)"""
        lst_of_fPHASE_object = read_input_file(fPcompare, Haplotype, "\t")
        #Change origin
        for fP_halpo in lst_of_fPHASE_object :
            fP_halpo.origin = "fPHASE"


        """Distribution of the occurence of haplotype hmz during the first run"""
         #Creation of the rigth dictionnary
        for fP_halpo in lst_of_fPHASE_object :
            fP_halpo.half_similarity_with = fP_halpo.similar_with_size(threshold)
        #Find the half simmilarity with all the génotype or only the uncorfirmed
        for fP_halpo, geno in it.product(lst_of_fPHASE_object, lst_unconfirmed_genotype) :
            fP_halpo.select_similar_with(geno, threshold)
        for fP_halpo in lst_of_fPHASE_object :
            fP_halpo.similar_occurence = fP_halpo.similarity_time_with()
            fP_halpo.frequency = fP_halpo.similarity_frequency(len(lst_of_geno_object))
        haplotype_redundancy(os.path.join(fastPHASE_dir, "fastPHASE_Haplotypes_redundancy"), lst_of_fPHASE_object)

        """Find which fP_haplo look like a Known Haplotype and a Candidate Haplotype"""
        #1- compare sequence (si = mettre dans un attribut l'instance de l'Haplotype Known, idem pour Candidate)
        #for fP_haplo, K_haplo in it.product(lst_of_fPHASE_object, lst_of_haplo_object) :
            #selecionné ce à 0 différence et trouvé un output a faire
        #2- faire un output 

        """Output rank of Known/candidate Haplotypes"""
        #pour chaque listes d'Haplotypes, je rempli haplo.half_similarity_with avec les géno. un len(du dico[0])
        #est ce que je tiens compte du threshold?


        """Acp de fastPhase si -p ==True"""
        #avec le fichier fourni avec -f
        #prendre en compte le bonne argument, faire le script (peut-être refaire le script pca_script pour l'adapter à celui-ci quitte a lancer 3fois la lecture)
        """distribution GvfH si -d ==True"""
        #need compare GvfH
        #prendre en compte le t choisi?
        

        """Venn-Diagramm Known/Candidaite/fastPHASE"""
        #need the 3 list : lst_of_haplo_object, lst_of_haplo_object_expanded_filter, lst_of_fPHASE_object ATTENTION sur quoi je les compare (name, sequence? maybe sequence)

        run5_end = time.time()
        time5 = run5_end - run5_start
        print ("Your comparation is over.")
        print("it's spend {}".format(time5))