import sys
import os
import numpy
from numpy import array
import moments
import pylab
from datetime import datetime
import Optimize_Functions
from moments import Misc,Spectrum,Numerics,Manips,Integration,Demographics1D,Demographics2D

# inumpy.t data dictionary, first argument
infile=sys.argv[1]
# pops id (as in data dictionary), aguments 2 and 3
pop_ids=[sys.argv[2],sys.argv[3]]
#projection sizes, in ALLELES not individuals, arguments 4 and 5
#projections=[int(sys.argv[4]),int(sys.argv[5])]

'''
Citations:
 If you use these scripts for your work, please cite the following publication:
 
 1-	The original publication that implemented this optimization strategy:
    Portik, D.M., Leach, A.D., Rivera, D., Blackburn, D.C., Rdel, M.-O.,
    Barej, M.F., Hirschfeld, M., Burger, M., and M.K.Fujita. 2017.
    Evaluating mechanisms of diversification in a Guineo-Congolian forest
    frog using demographic model selection. Molecular Ecology 26: 52455263.
    doi: 10.1111/mec.14266
 2-	The publication in which the optimization strategy was adapted to moments, 
 and models including bottlnecks and ancestral population size changes were first 
 introduced
 	Momigliano, P; Florin, Ann-Britt  and  Merilä, Juha. 2021. Biases in Demographic 
	Modeling Affect Our Understanding of Recent Divergence.
	Molecular Biology and Evolution38(7): 2967–2985. doi 10.1093/molbev/msab047

'''

#===========================================================================
# Import data to create joint-site frequency spectrum
#===========================================================================

#**************

data = moments.Spectrum.from_file ( infile )
numpy.set_printoptions(precision=3)


 


#print some useful information about the afs or jsfs
print "\n\n============================================================================\nData for site frequency spectrum\n============================================================================\n"
# print "projection", projections
print "sample sizes", data.sample_sizes
sfs_sum = numpy.around(data.S(), 2)
print "Sum of SFS = ", sfs_sum, '\n', '\n'



def SC(params, ns):
    """
    nu1= pop size for North Sea
	nu2=pop size for Baltic Sea 
	T1= time of population split
	T2= time of secondary contact
	m12= migration rate from North Sea to Baltic
	m21= migration rate from Baltic Sea to North Sea
    """
    nu1,nu2,T1,T2,m12,m21 = params

    sts = moments.LinearSystem_1D.steady_state_1D(ns[0] + ns[1])
    fs = moments.Spectrum(sts)
    fs = moments.Manips.split_1D_to_2D(fs, ns[0], ns[1])
    fs.integrate([nu1, nu2], T1, m = numpy.array([[0, 0], [0, 0]]))
    fs.integrate([nu1, nu2], T2, dt_fac=0.01, m=numpy.array([[0, m12], [m21, 0]]))
    return fs

p_labels = "nu1,nu2,T1,T2,m12,m21"
upper = [20,20,10,10,100,100]
lower = [1e-3,1e-3,1e-3,1e-3,1e-5,1e-5]

reps = [20,20,20]
maxiters = [10,20,30]
folds = [3,2,1]
for i in range(4,6):
	prefix = infile+"_OPTI_Number_{}".format(i)
	Optimize_Functions.Optimize_Routine(data, prefix, "SC", SC, 3, 6, data_folded=True, param_labels = p_labels, in_upper=upper, in_lower=lower, reps = reps, maxiters = maxiters, folds = folds)
