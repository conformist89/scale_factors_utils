import json
import argparse


parser = argparse.ArgumentParser(description="Plot the tau ID SF")
parser.add_argument("--wp", type=str, default="tight", help="TauID WP")
parser.add_argument("--era", type=str, default="2018", help="2016, 2017 or 2018")
parser.add_argument("--channel", type=str, default="mt", help="mt, et, em , tt")
parser.add_argument("--round_to", type=int, default=4, help="")
parser.add_argument("--user_out_tag", type=str, default="tight_2018UL", help="user_out_tag")
# parser.add_argument("--cat_number", type=int, default="1", help="differential categoty number")


args = parser.parse_args()


categories = ["DM0", "DM1", "DM10_11", "Inslusive", "Pt20to25", "Pt25to30", "Pt30to35", "Pt35to40", "PtGt40"]

cats = {

1 : "Pt20to25" ,
2 : "Pt25to30" ,
3 : "Pt30to35" ,
4 : "Pt35to40" ,
5 : "PtGt40" ,
6 : "Inslusive", 
7 : "DM0",
8 : "DM1", 
9 : "DM10_11"


}


# categories = ["DM0", "DM1", "DM10_11", "Inslusive", "Pt20to25", "Pt25to30", "Pt30to35", "Pt35to40","Pt40to60", "PtGt60"]

# cats = {

# 1 : "Pt20to25" ,
# 2 : "Pt25to30" ,
# 3 : "Pt30to35" ,
# 4 : "Pt35to40" ,
# 5 : "Pt40to60" ,
# 6 : "PtGt60" ,
# 7 : "Inslusive", 
# 8 : "DM0",
# 9 : "DM1", 
# 10 : "DM10_11"


# }

# json_sfs = "/work/olavoryk/sim_fit/smhtt_ul/Tau_"+str(args.wp)+"_"+str(args.era)+"UL_"+str(args.channel)+"_"+str(args.user_out_tag)+".json"

json_sfs = "/work/olavoryk/tau_pog_tau_sfs/tauid_multifit/smhtt_ul/Tau_"+str(args.wp)+"_"+str(args.era)+"UL_"+str(args.channel)+"_"+str(args.user_out_tag)+".json"



# if args.wp == "tight":
#   json_sfs = "/work/olavoryk/tauID_SF_ES/smhtt_ul/Tau.json"







with open(json_sfs, 'r') as f:
  data = json.load(f)

pt_binned_data = data["corrections"][0]

content = pt_binned_data["data"]["content"][0]

content1 = content['value']['content']

pt_range = [ 20.0, 25.0, 30.0, 35.0, 40.0, 10000.0 ]
# pt_range = [ 20.0, 25.0, 30.0, 35.0, 40.0, 60.0, 10000.0 ]

roundnumber = args.round_to


up_list = []
down_list = []
nom_list = []

for element in content1:
    print("\n  Nom: ", round(element['content'][0]['value'],roundnumber))

    print(" Up: ", round(element['content'][1]['value'] - element['content'][0]['value'],roundnumber))
    print(" down: ", round(element['content'][0]['value'] - element['content'][2]['value'],roundnumber))

    up_list.append(round(element['content'][1]['value'] - element['content'][0]['value'],roundnumber))
    down_list.append(round(element['content'][0]['value'] - element['content'][2]['value'],roundnumber))
    nom_list.append( round(element['content'][0]['value'],roundnumber) )

    print(str(round(element['content'][0]['value'],roundnumber))+'$^{+'+str(round(element['content'][1]['value'] - element['content'][0]['value'],roundnumber))+'}_{-'+str(round(element['content'][0]['value'] - element['content'][2]['value'],roundnumber))+'}$')


print("Nominal value: ", nom_list)
print("Upper unc list: ", up_list)
print("Down unc list: ", down_list)

correction_lib_list = []

for i in range(len(nom_list)):
  correction_lib_list.append( (nom_list[i], up_list[i], down_list[i]) )

print("\n This is correctionlib information: \n")
print(correction_lib_list)
print("\n ")




dm_binned_data = data["corrections"][1]

content = dm_binned_data["data"]["content"][0]

content2 = content['value']['content']


dm_dict = {}

dm_corrlib_list = []

for element in content2:
  print("\n DM nom: ", round( element['value']['content'][0]['value'],roundnumber )) 
  print(" DM up: ", round( element['value']['content'][1]['value'] - element['value']['content'][0]['value'], roundnumber )) 
  print(" DM down: ", round( element['value']['content'][0]['value'] - element['value']['content'][2]['value'], roundnumber )) 
  dm_corrlib_list.append(  (round( element['value']['content'][0]['value'],roundnumber ), round( element['value']['content'][1]['value'] - element['value']['content'][0]['value'], roundnumber ), round( element['value']['content'][0]['value'] - element['value']['content'][2]['value'], roundnumber ))  )


dm_dict[0] = dm_corrlib_list[0]
dm_dict[1] = dm_corrlib_list[1]
dm_dict[10] = dm_corrlib_list[2]
dm_dict[11] = dm_corrlib_list[3]


print("\n DM correctionlib information :", dm_dict)