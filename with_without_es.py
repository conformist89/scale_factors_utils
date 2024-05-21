import matplotlib.pyplot as plt
import argparse 
import numpy as np
from scipy.stats import chisquare
import os 

dm_x = ["1 Prong", "1 Prong + $\pi^{0}$", "3 Prong"]


sep_fit_cent = [0.9526021480560303, 1.024766206741333, 0.9499070644378662]
sep_fit_up = [0.9857621788978577, 1.0527935028076172, 0.9816796183586121 ]
sep_fit_down = [0.9202938675880432, 0.9976065754890442, 0.9180581569671631]

sep_fit_up_err = list(map(lambda x, y: x - y, sep_fit_up, sep_fit_cent))
sep_fit_down_err = list(map(lambda x, y: x - y, sep_fit_cent, sep_fit_down))


print(sep_fit_up_err)
print(sep_fit_down_err)


sim_fit_cent = [0.994, 1.089, 1.06,]
sim_fit_up = [0.046, 0.043, 0.038]
sim_fit_down = [0.089, 0.04, 0.038]

working_point = "medium"


def plot_sfs_dm(working_point, out_folder, era):

    deltax = 0.1

    asym_error_sim_fit = np.array(list(zip(sim_fit_down, sim_fit_up))).T

    asym_error_sep_fit = np.array(list(zip(sep_fit_down_err, sep_fit_up_err))).T
    

    f,a0 = plt.subplots(figsize=(10, 6))


    plt.grid()
    a0.errorbar([0-deltax, 1-deltax, 2-deltax, ], sim_fit_cent, yerr=asym_error_sim_fit, fmt='.', label = r'TauID {work_p} + ES comb. fit'.format(work_p = str(working_point))+' $D_{jet}$', color="darkblue", marker = "^")
    a0.errorbar([0+deltax, 1+deltax, 2+deltax, ], sep_fit_cent, yerr=asym_error_sep_fit, fmt='.', label = r'TauID {work_p} fit'.format(work_p = str(working_point))+' $D_{jet}$', color="magenta", marker = "^")
    a0.set_xlabel("$p_{T}($"+r"$\tau$"+"$_{h})$[GeV]")
    a0.set_ylabel("Correction factor")

    lumi = "0"
    if era == "2016preVFP":
        lumi = "19.5"  
    elif era == "2016postVFP":
        lumi = "16.8"
    elif era == "2017":
        lumi = "41.529"
    elif era == "2018":
        lumi = "59.83"

    
    a0.set_title('CMS $Preliminary$ ', loc='left')
    a0.set_title(era+  "_UL "+ lumi+ ' fb$^{-1}$  (13 TeV)', loc='right')
    a0.set_ylim(0.8, 1.2)
    a0.axhline(y = 1, color = 'salmon', linestyle = 'dashed')



    plt.setp(a0, xticks=[0, 1, 2, ], xticklabels=dm_x)




    a0.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    f.tight_layout()
    plt.savefig(out_folder+working_point+"_dm_sim_fit_vs_diff_fit_dm_with_without_es.pdf", dpi=300)
    plt.savefig(out_folder+working_point+"_dm_sim_fit_vs_diff_fit_dm_with_without_es.png", dpi=300)

out_folder="fold/"

if not os.path.exists(out_folder):
   os.makedirs(out_folder)

plot_sfs_dm(working_point, out_folder, "2016postVFP")