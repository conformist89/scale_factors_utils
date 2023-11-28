import ROOT
import os 

file_shapes = ROOT.TFile.Open("/work/olavoryk/tau_pog_tau_sfs/tauid_multifit/smhtt_ul/output/tight-2016postVFP-mt-2016postVFP_meas_tauid_v1-tight_vs_ele_id_es_v3/synced/htt_mt.inputs-sm-Run2016-ML.root", "read")

def plot_values():
    categories = []
    for k in file_shapes.GetListOfKeys():
        cat = k.ReadObj()
        category = cat.GetName()
        # print(category)
        categories.append(category)
    for cat in range(len(categories)):
        shapes_list = []
        for i in range(len(file_shapes.Get(str(categories[cat])).GetListOfKeys())):
            shapes_list.append(file_shapes.Get(categories[cat]).GetListOfKeys()[i].GetName())
        # print(shapes_list)

        for i in range(len(shapes_list)):
            pairs = []
            if "Down" in shapes_list[i]:
                shapes_list[i][:-4] == shapes_list[i+1][:-2]
                pairs.append(shapes_list[i])
                pairs.append(shapes_list[i+1])
                nom  = pairs[0][:pairs[0].find("CMS")-1]
                pairs.append(nom)
                # print(pairs)

                canv = ROOT.TCanvas("c", "c", 800, 600)
                down_shape = file_shapes.Get(categories[cat]).Get(pairs[0])
                up_shape = file_shapes.Get(categories[cat]).Get(pairs[1])
                nominal = file_shapes.Get(categories[cat]).Get(pairs[2])

                ratio_up = up_shape.Clone()
                ratio_up.Divide(nominal)

                ratio_down = down_shape.Clone()
                ratio_down.Divide(nominal)

                ratio_up.SetLineColor(ROOT.kRed)
                ratio_down.SetLineColor(ROOT.kBlue)

                ratio_up.SetTitle(pairs[0][:-4])
                ratio_down.SetTitle(pairs[0][:-4])

                legend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
                legend.AddEntry(ratio_up, "up", "l")
                legend.AddEntry(ratio_down, "down", "l")


                ratio_up.Draw()
                ratio_down.Draw("same")
                legend.Draw("same")
                canv.Draw()
                directory = "/home/olavoryk/helper/2016UL/up_dow_unc_ratio/"+str(categories[cat])+"/"
                if not os.path.exists(directory):
                    os.makedirs(directory)
                canv.SaveAs(directory+str(categories[cat])+"_"+pairs[0][:-4]+".png")


plot_values()