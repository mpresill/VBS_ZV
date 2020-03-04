# cuts
# cuts = {}
#Different supercut used

#supercut for test on succesive selections

supercut = 'nFatJet == 1 && abs(Alt$(FatJet_eta[0],-9999.))<2.4 && Alt$(FatJet_pt[0],0.)>200 && Alt$(FatJet_mass[0],0.)>65 && Alt$(FatJet_mass[0]<105,0.) &&\
            nLepton == 2 && nCleanJet > 1 &&\
            (Lepton_pdgId[0]*Lepton_pdgId[1] == - 11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == - 13*13) &&\
            mll>75 && mll<105 &&\
            Alt$(Lepton_pt[0],0.)>30 && Alt$(Lepton_pt[1],0.)>30  && mjj >800 && detajj > 3.5\
            && abs(Alt$(CleanJet_eta[1],-9999.))<5 && abs(Alt$(CleanJet_eta[0],-9999.))<5\
            && fabs(Alt$(Lepton_eta[0],-9999.))<2.5 && fabs(Alt$(Lepton_eta[1],-9999.))<2.5 && Alt$(CleanJet_pt[0],-9999.) >30 && Alt$(CleanJet_pt[1],-9999.) >30'

cuts['all'] = '1.'


#n.b.  Alt$(,0.) oppure Alt$(,-9999.) serve per non far spaccare il python se non trova un fat jet nell'evento

#zlep='\
#(abs((Alt$(Lepton_eta[0],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75) \
#&&(abs((Alt$(Lepton_eta[1],-9999.) - (Alt$(CleanJet_eta[0],-9999.)+Alt$(CleanJet_eta[1],-9999.))/2)/abs(detajj)) < 0.75)'

