#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (--ih <haplo_file>) (--ig <geno_file>)
    __main__.py (--ih <haplo_file>) (--ig <geno_file>) [-o <filename>] [-t <nb>] [-d] [-p] [-f <fP_file>] [-c]

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
    -p, --ACP                               Produce pca graphics based on inputs and outputs files.
                                            [default: False]
    -f <fP_file>, --fastPHASE <fP_file>     Compare your result by fastPHASE one
    -c, --cytoscape                         Produce file usable for the construction of an interaction network between G & H
                                            [default: False]

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
 
    # Parse arguments, use file docstring as a parameter definition
    arguments = docopt(__doc__, version='Haplotype rebuilding 0.3')
    print (arguments)

    haplotype_file = arguments["--ih"]
    genootype_file = arguments["--ig"]
    output = arguments["--output"]
    threshold = arguments["--threshold"]
    distribution = arguments["--dist"]
    pca = arguments["--ACP"]
    fPcompare = arguments["--fastPHASE"]
    cytoscape = arguments["--cytoscape"]

    
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
        geno.lst_of_new_haplotype = geno.have_new_haplotype_test() 
        geno.number_of_new_created_haplotype = len(geno.lst_of_new_haplotype)


    #Here the list of candidates Haplotypes objects
    lst_of_haplo_object_expanded = new_haplotype_test(lst_of_geno_object)
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
        new_haplo.similar_new_haplotype = new_haplo.screening_himself(lst_of_haplo_object_expanded)
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
    print("")
    
    ###RUN 1###
    print("")
    """Comparison of each genotype with each Hmz haplotype """
    compare_output(os.path.join(output, "run1_GvH"), lst_of_geno_object, lst_of_haplo_object)
    """A second output to see each similar Hmz haplotype of our Genotype in the Genotype object list"""#modification a faire ici car maintenant j'ai un dico
    compare_output_result(os.path.join(output, "run1_Compatible_Haplotypes"), lst_of_geno_object)#
    """A third output to see the new Haplotype created"""
    new_haplotype_output(os.path.join(output, "run1_candidates_Haplotypes"), lst_of_geno_object)# a indiquer combien de corerction il y a eut pour chaque Haplotype

    ###RUN 2###
    #Same output with new haplotype and the list of genotype not confirmed yet
    compare_output(os.path.join(output, "run2_GvH"), lst_genotype_non_confirmed, lst_of_haplo_object_expanded_filter)
    compare_output_result(os.path.join(output, "run2_Compatible_Haplotypes"), lst_genotype_non_confirmed)






    ###SUMMARY OUTPUT###
    #create the fonction and put it here



    run3_end = time.time()
    time3 = run3_end - run3_start
    print("Output_given")
    print("it's spend {}".format(time3))
