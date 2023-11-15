# scale_factors_utils
Complementary scripts for scale factors visual representation 

`read_sfs_json.py` is a script to retrieve tauid scale factors from json correctionlib file

Exaple of usage:

```
python3 read_sf_json.py --wp medium --era 2016preVFP --channel mt --round_to 5 --user_out_tag tauid_preVFP_v1
```

The user should specify `vs_jet` working poing `--wp` (tight/metium/loose/etc), data taking period `--era`,
the result could be rounded to the digit `--round_to` and tag which was used for scale factors computation
also should be used `--user_out_tag`     


Then one can plot scale factors as a function of pT and decay mode with the usage of `sim_fit_v1.py`:


```
python3 sim_fit_v1.py
```

scale factors should be copied as an input lists but this should be improved 