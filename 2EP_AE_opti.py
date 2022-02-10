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



def two_EP_ae(params, ns):
    """
    nu1= pop size following ancestral population expnasion )
	Tae= timing of ancestral population expansion
	T1= time of population split
	T2= time of secondary contact
	m12_0= migration rate from North Sea to Baltic
	m21_0= migration rate from Baltic Sea to North Sea
	m12= migration rate from North Sea to Baltic
	m21= migration rate from Baltic Sea to North Sea
    """
    nu_ae,nu1,nu2,Tae,T1,T2,m12a,m21a,m12b,m21b = params

    sts = moments.LinearSystem_1D.steady_state_1D(ns[0] + ns[1])
    fs = moments.Spectrum(sts)
    fs.integrate([nu_ae], Tae)
    fs = moments.Manips.split_1D_to_2D(fs, ns[0], ns[1])
    fs.integrate([nu1, nu2], T1, m = numpy.array([[0, m12a], [m21a, 0]]))
    fs.integrate([nu1, nu2], T2, dt_fac=0.01, m=numpy.array([[0, m12b], [m21b, 0]]))
    return fs


'''Optimization routine, controlling what happens
across each round. Let's keep the three rounds, but change the number of replicates,
the maxiter argument, and fold argument each time. We'll need to create a list of values
for each of these, that has three values within (to match three rounds).
'''

p_labels = "nu_ae,nu1,nu2,Tae,T1,T2,m12a,m21a,m12b,m21b"
upper = [20,20,20,10,10,10,100,100,100,100]
lower = [1e-3,1e-3,1e-3,1e-3,1e-3,1e-3,1e-5,1e-5,1e-5,1e-5]

reps = [20,20,20]
maxiters = [10,20,30]
folds = [3,2,1]
for i in range(4,6):
	prefix = infile+"_OPTI_Number_{}".format(i)
	Optimize_Functions.Optimize_Routine(data, prefix, "two_EP_ae", two_EP_ae, 3, 10, data_folded=True, param_labels = p_labels, in_upper=upper, in_lower=lower, reps = reps, maxiters = maxiters, folds = folds)
