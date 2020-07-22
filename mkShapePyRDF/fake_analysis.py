import ROOT as R

def analyse(rdf):

    rdf_ele = rdf.Filter("abs(Lepton_pdgId[0])==11")
    tight = rdf_ele.Filter("(Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5)")
    loose = rdf_ele.Filter("(Lepton_isTightElectron_mvaFall17V1Iso_WP90[0]<0.5 && Lepton_isTightMuon_cut_Tight_HWWW[0]<0.5)")

    h_T = tight.Histo1D(("hT", "Lepton_eta tight", 40, -3,3), "res_wjetcr_mjjincl_Lepton_eta", "weight_")
    h_L = loose.Histo1D(("hL", "Lepton_eta loose", 40, -3,3), "res_wjetcr_mjjincl_Lepton_eta", "weight_")
    h_All = rdf_ele.Histo1D(("hAll", "Lepton_eta all", 40,-3,3), "res_wjetcr_mjjincl_Lepton_eta", "weight_")

    c = R.TCanvas()
    h_All.Draw("hist")
    h_T.Draw("hist same")
    h_L.Draw("hist same")
    h_T.SetLineColor(R.kGreen)
    h_L.SetLineColor(R.kRed)
    c.Draw()

    c.SaveAs("Lepton_eta.png")

    return [h_T, h_L, h_All]

