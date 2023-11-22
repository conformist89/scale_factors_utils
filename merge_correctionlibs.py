import json
from os import path
import argparse
import yaml

file_path = "/work/olavoryk/tau_pog_tau_sfs/tauid_multifit/smhtt_ul/"

parser = argparse.ArgumentParser(description="Plot the tau ID SF")
parser.add_argument(
    "--era", type=str, default="2016postVFP", help="2016preVFP, 2016postVFP, 2017, 2018"
)
args = parser.parse_args()

channel = "mt"

working_points = [
    "vvvloose",
    "vvloose",
    "vloose",
    "loose",
    "medium",
    "tight",
    "vtight",
    "vvtight",
]



with open(
    "config_tags.yaml",
    "r",
) as stream:
    out = yaml.load(stream)
    user_out_tags = list(out[args.era].values())

user_out_tags = user_out_tags



def get_wp_json(working_point, era, channel, tag):
    json_file = (
        file_path
        + "Tau_"
        + str(working_point)
        + "_"
        + str(era)
        + "UL_"
        + str(channel)
        + "_"
        + str(tag)
        + ".json"
    )
    if path.exists(json_file):
        with open(json_file, "r") as file:
            json_data = json.load(file)
            return json_data["corrections"][0]["data"]["content"][0]
    else:
        print("File not found: ", json_file)
        return None


def get_wp_json_v1(working_points, era, channel, tags):
    lst_pt = []
    lst_dm = []
    for i in range(len(working_points)):
        json_file = (
            file_path
            + "Tau_"
            + str(working_points[i])
            + "_"
            + str(era)
            + "UL_"
            + str(channel)
            + "_"
            + str(tags[i])
            + ".json"
        )
        if path.exists(json_file):
            with open(json_file, "r") as file:
                json_data = json.load(file)
                lst_pt.append(json_data["corrections"][0]["data"]["content"][0])
                lst_dm.append(json_data["corrections"][1]["data"]["content"][0])
        else:
            print("File not found: ", json_file)
    # print(lst_dm)
    return lst_pt, lst_dm


def get_wp_json_v2(era, channel, lst_pt, lst_dm):
        json_file = (
            file_path
            + "Tau_"
            + str(working_points[0])
            + "_"
            + str(era)
            + "UL_"
            + str(channel)
            + "_"
            + str(user_out_tags[0])
            + ".json"
        )
        if path.exists(json_file):
            with open(json_file, "r") as file:
                json_data = json.load(file)
                json_data["corrections"][0]["data"]["content"][0] = lst_pt
                json_data["corrections"][1]["data"]["content"][0] = lst_dm
                with open('tauid_embedding_'+args.era+'.json', 'w') as f:
                    json.dump(json_data, f)


lst_pt, lst_dm = get_wp_json_v1(working_points, args.era, channel, user_out_tags)
get_wp_json_v2(args.era, channel, lst_pt, lst_dm)

