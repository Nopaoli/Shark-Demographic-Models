# Demographic modelling of grey reef sharks (*Carcharhinus amblyrhynchos*)
This repository contains the codes necessary to replicate the *moments* analyses from the following paper: 

Cameron Walsh*, Paolo Momigliano*, Germain Boussarie, William Robbins, Lucas Bonnin, Cecile Fauvelot, Jeremy Kiszka, David Mouillot, Laurent Vigliola, and Stéphanie Manel (2022). Genomic insights into the historical and contemporary demographics of the grey reef shark. *Heredity* XXX:XXX-XXX DOI: XXX 

co-first authors*

The pipeline used for demographic analyses is built based on the *dadi* pipeline by Portik et al (2017),  modified to work on *moments* by Momigliano et al (2021),  then by Alan le Moan (Le Moan et al 2021), and again modified by Paolo Momigliano for this manuscript. 

The files Model_2pop_folded.py and Model_2pop_unfolded.py contain the two population models to be used for folded and unfolded data, and are based on the models from Momigliano et al (2021). 

The files *Optimize_Functions.py* and *Summarize_Outputs.py* contain the scripts for the optmimization procedure and for summarising the results. They were developed by Daniel Portik, (Portik et al, 2017) to work with *dadi*, and then modified by Momigliano et al (2021) to work with *moments*. 

The Script_moments_model_optimisation_from_SFS.py can be used to run the entire optimization pipeline for each dataset and model. It's been modified from the script from Le Moan et al (2021). 

An example command to run 10 indepedent optimizations for the IM model using the shark data from our paper is: 

for i in {1. .10}
do
 python Script_moments_model_optimisation_from_SFS.py  -f indo-north_gbr.sfs  -x north_gbr -y indo -m IM -s True -r $i
done

Other relevant github repositories: 

https://github.com/alanlm-speciation/moments_optimization

https://github.com/dportik/dadi_pipeline

https://github.com/Nopaoli/Demographic-Modelling

Relevant citations: 

1-	Portik, D.M., Leach, A.D., Rivera, D., Blackburn, D.C., Rdel, M.-O., Barej, M.F., Hirschfeld, M., Burger, M., and M.K.Fujita (2017. Evaluating mechanisms of diversification in a Guineo-Congolian forest frog using demographic model selection. *Molecular Ecology* 26: 52455263. doi: 10.1111/mec.14266

2-	Momigliano, P.; Florin, A.B.  and  Merilä, J. 2021. Biases in Demographic  Modeling Affect Our Understanding of Recent Divergence. *Molecular Biology and Evolution*. 38(7): 2967–2985. doi 10.1093/molbev/msab047

3-  Le Moan, A., Bekkevold, D., & Hemmer-Hansen, J. (2021). Evolution at two time frames: ancient structural variants involved in post-glacial divergence of the European plaice (Pleuronectes platessa). Heredity, 126(4), 668-683.


