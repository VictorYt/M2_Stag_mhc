#!/usr/bin/python3.4
# -*- coding: utf-8 -*-


"""
usage: 
    __main__.py (--ih <haplo_file>) (--ig <geno_file>)
    __main__.py (--ih <haplo_file>) (--ig <geno_file>) [-o <filename>] [-t <nb>] [-d] [-p] [-c]

options:
    -h, --help                              This help.
    -v, --version                           Displays program's version.
    --ih <haplo_file>                       Haplotype input file
    --ig <geno_file>                        Genotype input file
    -o <filename>, --output <filename>      Output Name
                                            [default: Output_data]
    -t <nb>, --threshold <nb>               Threshold of accepted errors during haplotype and genotype comparaison 
                                            [default: 0]
    -d, --dist                              Produce distribution graphics based on inputs and outputs files. 
                                            [default: False]
    -p, --ACP                               Produce pca graphics based on inputs and outputs files.
                                            [default: False]
    -c, --cytoscape                         Produce the cytoscape file 
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
    arguments = docopt(__doc__, version='Haplotype rebuilding 0.1')
    print (arguments)

    distribution = arguments["--dist"]
    pca = arguments["--ACP"]
    output = arguments["--output"]
    threshold = arguments["--threshold"]
    haplotype_file = arguments["--ih"]
    genootype_file = arguments["--ig"]
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

    """Construction of the list of Haplotype object"""
    lst_of_haplo_object = read_input_file(haplotype_file, Haplotype, "\t")
    #print ("Haplotype number :",len(lst_of_haplo_object))
    """Construction of my list of Genotype object"""
    lst_of_geno_object = read_input_file(genootype_file, Genotype, ",")
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
    for geno, haplo in it.product(lst_of_geno_object, lst_of_haplo_object):
        geno.select_similar_haplotype(geno, haplo) 
        geno.number_of_similar_haplotype = len(geno.similar_haplotype)


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

    nb_new_h = 0 #a counter
    for geno in lst_of_geno_object :
        #What haplotypes combined with another give us our genotype
        geno.probable_haplotypes_combinaison = geno.combinaison_between_similar_haplotype_in_geno()
        geno.number_of_probable_haplotypes_combinaison = len(geno.probable_haplotypes_combinaison)
        #New Haplotype creation, store in the genotype attribut : lst_of_new_haplotype
        geno.lst_of_new_haplotype = geno.have_new_haplotype() 
        geno.number_of_new_created_haplotype = len(geno._lst_of_new_haplotype)

        #Sum counter
        nb_new_h += geno.number_of_new_created_haplotype
    print ("Number of new haplotype created : {}".format(nb_new_h))


    #Here the list of new Haplotype object
    lst_of_haplo_object_expanded = new_haplotype(lst_of_geno_object)


    run1_end = time.time()
    time1 = run1_end - run1_start
    print("1st run ending")
    print("it's spend {}".format(time1))


    ##############
    ##SECOND RUN##
    ##############
    run2_start = time.time()

    """Screening of identical new Haplotypes"""
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
    print("Number of new Haplotype after screening : {}".format(len(lst_of_haplo_object_expanded_filter)))

    
    """Reduction of the Genotype list"""
    lst_genotype_confirmed = []
    lst_genotype_non_confirmed = []
    #Are removed genotypes with at least one combination of haplotype
    for geno in lst_of_geno_object :
        if geno.number_of_new_created_haplotype == 0 and geno.number_of_similar_haplotype > 1 :
            lst_genotype_confirmed.append(geno)
        else : 
            lst_genotype_non_confirmed.append(geno)



    print ("Number of Genotype who can be explain by our list of Haplotypes : {}".format(len(lst_genotype_confirmed)))
    print ("Another {} unconfirmed Genotypes ".format(len(lst_genotype_non_confirmed)))




    #Here we make a list of all Haplotypes objects
    lst_of_haplo_object_all = lst_of_haplo_object + lst_of_haplo_object_expanded

    #Add to Haplotypes objets missing_data occurence in there sequence
    for haplo in lst_of_haplo_object_all :
        haplo.missing_data_counter()


    #Add new_haplotype which are similar to our genotype no confirmed, in the list of similar_haplotype
    for geno_non_confirmed, new_haplo in it.product(lst_genotype_non_confirmed, lst_of_haplo_object_expanded_filter):
        geno_non_confirmed.select_similar_haplotype(geno_non_confirmed, new_haplo)
        geno_non_confirmed.number_of_similar_haplotype = len(geno_non_confirmed.similar_haplotype)


    """Again, after finding similar haplotypes to our genotypes, 
    we combine these haplotypes to see if they explain our genotype."""
    #Here we don't create new haplotype (They will bring more false positive than after the 1st run)
    for geno in lst_genotype_non_confirmed :
        #What haplotypes combined with another give us our genotype
        geno.probable_haplotypes_combinaison_2_run = geno.combinaison_between_similar_haplotype_in_geno()
        geno.number_of_probable_haplotypes_combinaison_2_run = len(geno.probable_haplotypes_combinaison_2_run)


    run2_end = time.time()
    time2 = run2_end - run2_start
    print("2nd run ending")
    print("it's spend {}".format(time2))


    ##############
    ##OUTPUT RUN##
    ##############
    run3_start = time.time()
    

    ###RUN 1###
    """Comparison of each genotype with each Hmz haplotype """
    compare_output(os.path.join(output, "run1_GvH"), lst_of_geno_object, lst_of_haplo_object)
    """A second output to see each similar Hmz haplotype of our Genotype in the Genotype object list"""
    compare_output_result(os.path.join(output, "run1_Compatible_Haplotypes"), lst_of_geno_object)
    """A third output to see the new Haplotype created"""
    new_haplotype_output(os.path.join(output, "run1_New_Haplotypes"), lst_of_geno_object)

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




    # Look at distribution argument
    if (distribution == True):
        print ("-dist utilisé")

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
        """The distribution of the run1_GvH"""
        error_distribution_output(os.path.join(dist,"GvH_distribution"), error_distribution(lst_of_haplo_object, os.path.join(output,"run1_GvH")))
        
        """The distribution of the run1_HvH"""
        compare_output(os.path.join(dist, "run1_HvH"), lst_of_haplo_object, lst_of_haplo_object)
        error_distribution_output(os.path.join(dist, "HvH_distribution"), error_distribution(lst_of_haplo_object_expanded_filter, os.path.join(dist,"run1_HvH")))

        """Distribution of the occurrence of new haplotypes during the second run"""
        new_haplotype_occurency(os.path.join(dist, "new_Haplotypes_occ"), lst_of_haplo_object_expanded_filter, lst_genotype_non_confirmed)

    #############
    ##GRAPHIQUE##
    #############
        #And now the functions using subprocess to collect distribution pdf
        run_R_file("barplot_distribution.R", dist)
        #The violin dotplot & occurency of missing data
        run_R_file("geom_dotplot_violin.R", dist)











    # Look at pca argument
    if (pca == True):
        print ("-p utilisé")

        pca = os.path.join(dirname, "ACP")

        try:
            os.makedirs(pca)
        except OSError:
            if os.path.exists(pca):
            # We are nearly safe
                pass
            else:
            # There was an error on creation, so make sure we know about it
                raise


    # Look at cytoscape argument
    if (cytoscape == True):
        print ("-c utilisé")

        cytoscape = os.path.join(dirname, "Cytoscape")

        try:
            os.makedirs(cytoscape)
        except OSError:
            if os.path.exists(cytoscape):
            # We are nearly safe
                pass
            else:
            # There was an error on creation, so make sure we know about it
                raise
