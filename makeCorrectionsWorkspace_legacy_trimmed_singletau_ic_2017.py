#!/usr/bin/env python
import ROOT
import imp
from array import array
import numpy as np
import math

wsptools = imp.load_source('wsptools', 'workspaceTools.py')

def GetFromTFile(str):
    f = ROOT.TFile(str.split(':')[0])
    obj = f.Get(str.split(':')[1]).Clone()
    f.Close()
    return obj

# Boilerplate
ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.RooWorkspace.imp = getattr(ROOT.RooWorkspace, 'import')
ROOT.TH1.AddDirectory(0)

w = ROOT.RooWorkspace('w')

## electron
loc = 'inputs/2017/ICSF/'

histsToWrap = [
    (loc+'singleElec/electron_SFs.root:data_trg_eff', 'e_trg_ic_data'),
    (loc+'singleElec/electron_SFs.root:ZLL_trg_eff', 'e_trg_ic_mc'),
    (loc+'singleElec/electron_SFs.root:embed_trg_eff', 'e_trg_ic_embed'),
    (loc+'singleElec/aiso1/electron_SFs.root:data_trg_eff', 'e_trg_aiso1_ic_data'),
    (loc+'singleElec/aiso1/electron_SFs.root:ZLL_trg_eff', 'e_trg_aiso1_ic_mc'),
    (loc+'singleElec/aiso1/electron_SFs.root:embed_trg_eff', 'e_trg_aiso1_ic_embed'),
    (loc+'singleElec/aiso2/electron_SFs.root:data_trg_eff', 'e_trg_aiso2_ic_data'),
    (loc+'singleElec/aiso2/electron_SFs.root:ZLL_trg_eff', 'e_trg_aiso2_ic_mc'),
    (loc+'singleElec/aiso2/electron_SFs.root:embed_trg_eff', 'e_trg_aiso2_ic_embed'),

    (loc+'ET/electron_SFs.root:data_trg_eff', 'e_trg_24_ic_data'),
    (loc+'ET/electron_SFs.root:ZLL_trg_eff', 'e_trg_24_ic_mc'),
    (loc+'ET/electron_SFs.root:embed_trg_eff', 'e_trg_24_ic_embed'),
    (loc+'ET/aiso1/electron_SFs.root:data_trg_eff', 'e_trg_24_aiso1_ic_data'),
    (loc+'ET/aiso1/electron_SFs.root:ZLL_trg_eff', 'e_trg_24_aiso1_ic_mc'),
    (loc+'ET/aiso1/electron_SFs.root:embed_trg_eff', 'e_trg_24_aiso1_ic_embed'),
    (loc+'ET/aiso2/electron_SFs.root:data_trg_eff', 'e_trg_24_aiso2_ic_data'),
    (loc+'ET/aiso2/electron_SFs.root:ZLL_trg_eff', 'e_trg_24_aiso2_ic_mc'),
    (loc+'ET/aiso2/electron_SFs.root:embed_trg_eff', 'e_trg_24_aiso2_ic_embed'),
]

for task in histsToWrap:
    wsptools.SafeWrapHist(w, ['e_pt', 'expr::e_abs_eta("TMath::Abs(@0)",e_eta[0])'],
                          GetFromTFile(task[0]), name=task[1])

wsptools.MakeBinnedCategoryFuncMap(w, 'e_iso', [0., 0.15, 0.25, 0.50],
                                   'e_trg_binned_ic_data', ['e_trg_ic_data', 'e_trg_aiso1_ic_data', 'e_trg_aiso2_ic_data'])
wsptools.MakeBinnedCategoryFuncMap(w, 'e_iso', [0., 0.15, 0.25, 0.50],
                                   'e_trg_binned_ic_mc', ['e_trg_ic_mc', 'e_trg_aiso1_ic_mc', 'e_trg_aiso2_ic_mc'])
wsptools.MakeBinnedCategoryFuncMap(w, 'e_iso', [0., 0.15, 0.25, 0.50],
                                   'e_trg_binned_ic_embed', ['e_trg_ic_embed', 'e_trg_aiso1_ic_embed', 'e_trg_aiso2_ic_embed'])

wsptools.MakeBinnedCategoryFuncMap(w, 'e_iso', [0., 0.15, 0.25, 0.50],
                                   'e_trg_24_binned_ic_data', ['e_trg_24_ic_data', 'e_trg_24_aiso1_ic_data', 'e_trg_24_aiso2_ic_data'])
wsptools.MakeBinnedCategoryFuncMap(w, 'e_iso', [0., 0.15, 0.25, 0.50],
                                   'e_trg_24_binned_ic_mc', ['e_trg_24_ic_mc', 'e_trg_24_aiso1_ic_mc', 'e_trg_24_aiso2_ic_mc'])
wsptools.MakeBinnedCategoryFuncMap(w, 'e_iso', [0., 0.15, 0.25, 0.50],
                                   'e_trg_24_binned_ic_embed', ['e_trg_24_ic_embed', 'e_trg_24_aiso1_ic_embed', 'e_trg_24_aiso2_ic_embed'])

## muon
loc = 'inputs/2017/ICSF/'

histsToWrap = [
    (loc+'singleMu/muon_SFs.root:data_trg_eff', 'm_trg_ic_data'),
    (loc+'singleMu/muon_SFs.root:ZLL_trg_eff', 'm_trg_ic_mc'),
    (loc+'singleMu/muon_SFs.root:embed_trg_eff', 'm_trg_ic_embed'),
    (loc+'singleMu/aiso1/muon_SFs.root:data_trg_eff', 'm_trg_aiso1_ic_data'),
    (loc+'singleMu/aiso1/muon_SFs.root:ZLL_trg_eff', 'm_trg_aiso1_ic_mc'),
    (loc+'singleMu/aiso1/muon_SFs.root:embed_trg_eff', 'm_trg_aiso1_ic_embed'),
    (loc+'singleMu/aiso2/muon_SFs.root:data_trg_eff', 'm_trg_aiso2_ic_data'),
    (loc+'singleMu/aiso2/muon_SFs.root:ZLL_trg_eff', 'm_trg_aiso2_ic_mc'),
    (loc+'singleMu/aiso2/muon_SFs.root:embed_trg_eff', 'm_trg_aiso2_ic_embed'),

    (loc+'MT_B/muon_SFs.root:data_trg_eff', 'm_trg_20_runB_ic_data'),
    (loc+'MT_B/aiso1/muon_SFs.root:data_trg_eff', 'm_trg_20_aiso1_runB_ic_data'),
    (loc+'MT_B/aiso2/muon_SFs.root:data_trg_eff', 'm_trg_20_aiso2_runB_ic_data'),

    (loc+'MT_CtoF/muon_SFs.root:data_trg_eff', 'm_trg_20_runCtoF_ic_data'),
    (loc+'MT_CtoF/muon_SFs.root:ZLL_trg_eff', 'm_trg_20_ic_mc'),
    (loc+'MT_CtoF/muon_SFs.root:embed_trg_eff', 'm_trg_20_ic_embed'),
    (loc+'MT_CtoF/aiso1/muon_SFs.root:data_trg_eff', 'm_trg_20_aiso1_runCtoF_ic_data'),
    (loc+'MT_CtoF/aiso1/muon_SFs.root:ZLL_trg_eff', 'm_trg_20_aiso1_ic_mc'),
    (loc+'MT_CtoF/aiso1/muon_SFs.root:embed_trg_eff', 'm_trg_20_aiso1_ic_embed'),
    (loc+'MT_CtoF/aiso2/muon_SFs.root:data_trg_eff', 'm_trg_20_aiso2_runCtoF_ic_data'),
    (loc+'MT_CtoF/aiso2/muon_SFs.root:ZLL_trg_eff', 'm_trg_20_aiso2_ic_mc'),
    (loc+'MT_CtoF/aiso2/muon_SFs.root:embed_trg_eff', 'm_trg_20_aiso2_ic_embed'),

]

for task in histsToWrap:
    wsptools.SafeWrapHist(w, ['m_pt', 'expr::m_abs_eta("TMath::Abs(@0)",m_eta[0])'],
                          GetFromTFile(task[0]), name=task[1])

# weight runB and CtoF by lumi for data 
w.factory('expr::m_trg_20_ic_data("0.1145*@0+0.8855*@1", m_trg_20_runB_ic_data, m_trg_20_runCtoF_ic_data)')
w.factory('expr::m_trg_20_aiso1_ic_data("0.1145*@0+0.8855*@1", m_trg_20_aiso1_runB_ic_data, m_trg_20_aiso1_runCtoF_ic_data)')
w.factory('expr::m_trg_20_aiso2_ic_data("0.1145*@0+0.8855*@1", m_trg_20_aiso2_runB_ic_data, m_trg_20_aiso2_runCtoF_ic_data)')

wsptools.MakeBinnedCategoryFuncMap(w, 'm_iso', [0., 0.15, 0.25, 0.50],
                                   'm_trg_binned_ic_data', ['m_trg_ic_data', 'm_trg_aiso1_ic_data', 'm_trg_aiso2_ic_data'])
wsptools.MakeBinnedCategoryFuncMap(w, 'm_iso', [0., 0.15, 0.25, 0.50],
                                   'm_trg_binned_ic_mc', ['m_trg_ic_mc', 'm_trg_aiso1_ic_mc', 'm_trg_aiso2_ic_mc'])
wsptools.MakeBinnedCategoryFuncMap(w, 'm_iso', [0., 0.15, 0.25, 0.50],
                                   'm_trg_binned_ic_embed', ['m_trg_ic_embed', 'm_trg_aiso1_ic_embed', 'm_trg_aiso2_ic_embed'])

wsptools.MakeBinnedCategoryFuncMap(w, 'm_iso', [0., 0.15, 0.25, 0.50],
                                   'm_trg_20_binned_ic_data', ['m_trg_20_ic_data', 'm_trg_20_aiso1_ic_data', 'm_trg_20_aiso2_ic_data'])
wsptools.MakeBinnedCategoryFuncMap(w, 'm_iso', [0., 0.15, 0.25, 0.50],
                                   'm_trg_20_binned_ic_mc', ['m_trg_20_ic_mc', 'm_trg_20_aiso1_ic_mc', 'm_trg_20_aiso2_ic_mc'])
wsptools.MakeBinnedCategoryFuncMap(w, 'm_iso', [0., 0.15, 0.25, 0.50],
                                   'm_trg_20_binned_ic_embed', ['m_trg_20_ic_embed', 'm_trg_20_aiso1_ic_embed', 'm_trg_20_aiso2_ic_embed'])

# deepTau ID SFs

loc = 'inputs/2017/TauPOGTriggerSFs/'
tau_trg_file = ROOT.TFile(loc+'2017_tauTriggerEff_DeepTau2017v2p1.root')
#tau_id_wps=['VVVLoose','VVLoose','VLoose','Loose','Medium','Tight']
tau_id_wps=['Medium']#,'Tight']

for wp in tau_id_wps:
  for dm in ['0','1','10',11]:

    histsToWrap = [
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:data_mutau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_mutau_dm%s_data' % (wp.lower(),dm)),
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:mc_mutau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_mutau_dm%s_mc' % (wp.lower(),dm)),
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:sf_mutau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_mutau_dm%s_ratio' % (wp.lower(),dm)),
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:data_etau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_etau_dm%s_data' % (wp.lower(),dm)),
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:mc_etau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_etau_dm%s_mc' % (wp.lower(),dm)),
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:sf_etau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_etau_dm%s_ratio' % (wp.lower(),dm)),
    ]

    for task in histsToWrap:
        wsptools.SafeWrapHist(w, ['t_pt'],
                              GetFromTFile(task[0]), name=task[1])

        hist = GetFromTFile(task[0])
        uncert_hists = wsptools.UncertsFromHist(hist)
        wsptools.SafeWrapHist(w, ['t_pt'], uncert_hists[0], name=task[1]+'_up')
        wsptools.SafeWrapHist(w, ['t_pt'], uncert_hists[1], name=task[1]+'_down')

        if 'ditau' in task[1]:
          wsptools.SafeWrapHist(w, ['t_pt_2'],
                                GetFromTFile(task[0]), name=task[1]+'_2')
  
          hist = GetFromTFile(task[0])
          uncert_hists = wsptools.UncertsFromHist(hist)
          wsptools.SafeWrapHist(w, ['t_pt_2'], uncert_hists[0], name=task[1]+'_up_2')
          wsptools.SafeWrapHist(w, ['t_pt_2'], uncert_hists[1], name=task[1]+'_down_2') 

  wp_lower = wp.lower()
  for i in ['data','mc','ratio']:
    for j in ['mutau', 'etau']:
      taus=['']
      if j == 'ditau': taus = ['', '_2']
      for t in taus:
        w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s("(@0==0)*@1 + (@0==1)*@2 + (@0==10||@0==5)*@3 + (@0==11||@0==6)*@4", t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm0_%(i)s%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm1_%(i)s%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm10_%(i)s%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm11_%(i)s%(t)s)' % vars())

        w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_up%(t)s("@5 + ((@0==0)*@1 + (@0==1)*@2 + (@0==10||@0==5)*@3 + (@0==11||@0==6)*@4)", t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm0_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm1_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm10_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm11_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())

        w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_down%(t)s("@5 - ((@0==0)*@1 + (@0==1)*@2 + (@0==10||@0==5)*@3 + (@0==11||@0==6)*@4)", t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm0_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm1_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm10_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm11_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())

        for dm in ['0','1','10','11']:
          w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_dm%(dm)s_down%(t)s("(@0==%(dm)s)*@1 + (@0!=%(dm)s)*@2",t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())
          w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_dm%(dm)s_up%(t)s("(@0==%(dm)s)*@1 + (@0!=%(dm)s)*@2",t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())

### Tau Trigger scale factors from KIT - for using with deeptau IDs and for embedded samples

loc = 'inputs/2017/KIT/tau_trigger/'
tau_trg_file = ROOT.TFile(loc+'tauTriggerEfficiencies2017KIT_deeptau.root')
w.factory('expr::t_pt_trig("min(max(@0,20),450)" ,t_pt[0])')
#tau_id_wps=['vlooseDeepTau','looseDeepTau','mediumDeepTau','tightDeepTau','vtightDeepTau','vvtightDeepTau']
tau_id_wps=['mediumDeepTau']

for wp in tau_id_wps:
  for dm in ['0', '1', '10', '11']:
    histsToWrap = [
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:mutau_%s_dm%s_DATA' % (wp,dm),  't_trg_phieta_%s_mutau_dm%s_data' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:mutau_%s_dm%s_MC' % (wp,dm),  't_trg_phieta_%s_mutau_dm%s_mc' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:mutau_%s_dm%s_EMB' % (wp,dm),  't_trg_phieta_%s_mutau_dm%s_embed' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:mutau_%s_dm%s_DATA_AVG' % (wp,dm),  't_trg_ave_phieta_%s_mutau_dm%s_data' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:mutau_%s_dm%s_MC_AVG' % (wp,dm),  't_trg_ave_phieta_%s_mutau_dm%s_mc' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:mutau_%s_dm%s_EMB_AVG' % (wp,dm),  't_trg_ave_phieta_%s_mutau_dm%s_embed' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:etau_%s_dm%s_DATA' % (wp,dm),  't_trg_phieta_%s_etau_dm%s_data' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:etau_%s_dm%s_MC' % (wp,dm),  't_trg_phieta_%s_etau_dm%s_mc' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:etau_%s_dm%s_EMB' % (wp,dm),  't_trg_phieta_%s_etau_dm%s_embed' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:etau_%s_dm%s_DATA_AVG' % (wp,dm),  't_trg_ave_phieta_%s_etau_dm%s_data' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:etau_%s_dm%s_MC_AVG' % (wp,dm),  't_trg_ave_phieta_%s_etau_dm%s_mc' % (wp,dm)),
      (loc+'tauTriggerEfficiencies2017KIT_deeptau.root:etau_%s_dm%s_EMB_AVG' % (wp,dm),  't_trg_ave_phieta_%s_etau_dm%s_embed' % (wp,dm))
    ]
    for task in histsToWrap:
      wsptools.SafeWrapHist(w, ['t_eta','t_phi'],
                            GetFromTFile(task[0]), name=task[1])

for wp in tau_id_wps:
  for dm in ['0', '1', '10', '11']:
    for y in ['mutau','etau']:

      for x in ['data', 'mc', 'embed']:
        if not x is 'embed': func = tau_trg_file.Get("%s_%s_dm%s_%s_fit" % (y,wp,dm,x.upper()))
        else: func = tau_trg_file.Get("%s_%s_dm%s_EMB_fit" % (y,wp,dm))
        params = func.GetParameters()
        w.factory('expr::t_trg_pt_%s_%s_dm%s_%s("%.12f - ROOT::Math::crystalball_cdf(-@0, %.12f, %.12f, %.12f, %.12f)*(%.12f)", t_pt_trig)' % (wp,y,dm,x, params[5],params[0],params[1],params[2],params[3],params[4]))

for wp in tau_id_wps:
  for dm in ['0', '1', '10', '11']:
    for y in ['mutau','etau']:

      for x in ['data', 'mc', 'embed']:
        w.factory('expr::t_trg_phieta_%s_%s_%s("(@0==0)*@1 + (@0==1)*@2 + (@0==10)*@3 + (@0==11)*@4", t_dm[0], t_trg_phieta_%s_%s_dm0_%s, t_trg_phieta_%s_%s_dm1_%s, t_trg_phieta_%s_%s_dm10_%s, t_trg_phieta_%s_%s_dm11_%s)' % (wp, y, x, wp, y, x, wp, y, x, wp, y, x, wp, y, x))
        w.factory('expr::t_trg_ave_phieta_%s_%s_%s("(@0==0)*@1 + (@0==1)*@2 + (@0==10)*@3 + (@0==11)*@4", t_dm[0], t_trg_ave_phieta_%s_%s_dm0_%s, t_trg_ave_phieta_%s_%s_dm1_%s, t_trg_ave_phieta_%s_%s_dm10_%s, t_trg_ave_phieta_%s_%s_dm11_%s)' % (wp, y, x, wp, y, x, wp, y, x, wp, y, x, wp, y, x))

        w.factory('expr::t_trg_pt_%s_%s_%s("(@0==0)*@1 + (@0==1)*@2 + (@0==10)*@3 + (@0==11)*@4", t_dm[0], t_trg_pt_%s_%s_dm0_%s, t_trg_pt_%s_%s_dm1_%s, t_trg_pt_%s_%s_dm10_%s, t_trg_pt_%s_%s_dm11_%s)' % (wp, y, x, wp, y, x, wp, y, x, wp, y, x, wp, y, x))

        w.factory('expr::t_trg_%s_%s_%s("min(@0*@1/@2,1)", t_trg_pt_%s_%s_%s, t_trg_phieta_%s_%s_%s, t_trg_ave_phieta_%s_%s_%s)' % (wp, y, x, wp, y, x, wp, y, x, wp, y, x))

      w.factory('expr::t_trg_%s_%s_ratio("@0/@1", t_trg_%s_%s_data, t_trg_%s_%s_mc)' % (wp, y, wp, y, wp, y))
      w.factory('expr::t_trg_%s_%s_embed_ratio("@0/@1", t_trg_%s_%s_data, t_trg_%s_%s_embed)' % (wp, y, wp, y, wp, y))


# now use the histograms to get the uncertainty variations
for wp in tau_id_wps:
  for dm in ['0','1','10','11']:
     histsToWrap = [
      ('mutau_%s_dm%s_DATA_errorBand' % (wp,dm), 't_trg_uncert_%s_mutau_dm%s_data' % (wp,dm)),
      ('etau_%s_dm%s_DATA_errorBand' % (wp,dm), 't_trg_uncert_%s_etau_dm%s_data' % (wp,dm)),
      ('mutau_%s_dm%s_MC_errorBand' % (wp,dm), 't_trg_uncert_%s_mutau_dm%s_mc' % (wp,dm)),
      ('etau_%s_dm%s_MC_errorBand' % (wp,dm), 't_trg_uncert_%s_etau_dm%s_mc' % (wp,dm)),
      ('mutau_%s_dm%s_EMB_errorBand' % (wp,dm), 't_trg_uncert_%s_mutau_dm%s_embed' % (wp,dm)),
      ('etau_%s_dm%s_EMB_errorBand' % (wp,dm), 't_trg_uncert_%s_etau_dm%s_embed' % (wp,dm))
     ]

     for task in histsToWrap:
       hist = tau_trg_file.Get(task[0])
       uncert_hists = wsptools.UncertsFromHist(hist)
       wsptools.SafeWrapHist(w, ['t_pt_trig'], uncert_hists[0], name=task[1]+'_up')
       wsptools.SafeWrapHist(w, ['t_pt_trig'], uncert_hists[1], name=task[1]+'_down')

  for y in ['mutau','etau']:
    taus=['']
    for t in taus:
      for x in ['data', 'mc', 'embed']:
        w.factory('expr::t_trg_pt_uncert_%(wp)s_%(y)s_%(x)s_up%(t)s("(@0==0)*@1 + (@0==1)*@2 + (@0>=3&&@0<11)*@3 + (@0==11)*@4", t_dm%(t)s[0], t_trg_uncert_%(wp)s_%(y)s_dm0_%(x)s_up%(t)s, t_trg_uncert_%(wp)s_%(y)s_dm1_%(x)s_up%(t)s, t_trg_uncert_%(wp)s_%(y)s_dm10_%(x)s_up%(t)s, t_trg_uncert_%(wp)s_%(y)s_dm11_%(x)s_up%(t)s)'    % vars())
        w.factory('expr::t_trg_pt_uncert_%(wp)s_%(y)s_%(x)s_down%(t)s("(@0==0)*@1 + (@0==1)*@2 + (@0>=3&&@0<11)*@3 + (@0==11)*@4", t_dm%(t)s[0], t_trg_uncert_%(wp)s_%(y)s_dm0_%(x)s_down%(t)s, t_trg_uncert_%(wp)s_%(y)s_dm1_%(x)s_down%(t)s, t_trg_uncert_%(wp)s_%(y)s_dm10_%(x)s_down%(t)s, t_trg_uncert_%(wp)s_%(y)s_dm11_%(x)s_down%(t)s)' % vars())

        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_up%(t)s("(@0>0)*min((@0+@1)*@2/@0,1)", t_trg_pt_%(wp)s_%(y)s_%(x)s%(t)s, t_trg_pt_uncert_%(wp)s_%(y)s_%(x)s_up%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_down%(t)s("(@0>0)*max((@0-@1)*@2/@0,0)", t_trg_pt_%(wp)s_%(y)s_%(x)s%(t)s, t_trg_pt_uncert_%(wp)s_%(y)s_%(x)s_down%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())

      w.factory('expr::t_trg_%(wp)s_%(y)s_ratio_up%(t)s("(@1>0)*(@3>0)*(sqrt(pow((@0-@1)/@1,2) + pow((@2-@3)/@3,2))+1.)*@4",t_trg_%(wp)s_%(y)s_data_up%(t)s, t_trg_%(wp)s_%(y)s_data%(t)s, t_trg_%(wp)s_%(y)s_mc_up%(t)s, t_trg_%(wp)s_%(y)s_mc%(t)s, t_trg_%(wp)s_%(y)s_ratio%(t)s)' % vars())

      w.factory('expr::t_trg_%(wp)s_%(y)s_ratio_down%(t)s("(@1>0)*(@3>0)*(1.-sqrt(pow((@1-@0)/@1,2) + pow((@3-@2)/@3,2)))*@4",t_trg_%(wp)s_%(y)s_data_down%(t)s, t_trg_%(wp)s_%(y)s_data%(t)s, t_trg_%(wp)s_%(y)s_mc_down%(t)s, t_trg_%(wp)s_%(y)s_mc%(t)s, t_trg_%(wp)s_%(y)s_ratio%(t)s)' % vars())

      w.factory('expr::t_trg_%(wp)s_%(y)s_embed_ratio_up%(t)s("(@1>0)*(@3>0)*(sqrt(pow((@0-@1)/@1,2) + pow((@2-@3)/@3,2))+1.)*@4",t_trg_%(wp)s_%(y)s_data_up%(t)s, t_trg_%(wp)s_%(y)s_data%(t)s, t_trg_%(wp)s_%(y)s_embed_up%(t)s, t_trg_%(wp)s_%(y)s_embed%(t)s, t_trg_%(wp)s_%(y)s_embed_ratio%(t)s)' % vars())

      w.factory('expr::t_trg_%(wp)s_%(y)s_embed_ratio_down%(t)s("(@1>0)*(@3>0)*(1.-sqrt(pow((@1-@0)/@1,2) + pow((@3-@2)/@3,2)))*@4",t_trg_%(wp)s_%(y)s_data_down%(t)s, t_trg_%(wp)s_%(y)s_data%(t)s, t_trg_%(wp)s_%(y)s_embed_down%(t)s, t_trg_%(wp)s_%(y)s_embed%(t)s, t_trg_%(wp)s_%(y)s_embed_ratio%(t)s)' % vars())

      for x in ['ratio', 'embed_ratio', 'data', 'mc', 'embed']:
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm0_up%(t)s("(@0==0)*@1 + (@0!=0)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_up%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm0_down%(t)s("(@0==0)*@1 + (@0!=0)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_down%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm1_up%(t)s("(@0==1)*@1 + (@0!=1)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_up%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm1_down%(t)s("(@0==1)*@1 + (@0!=1)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_down%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm10_up%(t)s("(@0==10)*@1 + (@0!=10)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_up%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm10_down%(t)s("(@0==10)*@1 + (@0!=10)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_down%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm11_up%(t)s("(@0==11)*@1 + (@0!=11)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_up%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())
        w.factory('expr::t_trg_%(wp)s_%(y)s_%(x)s_dm11_down%(t)s("(@0==11)*@1 + (@0!=11)*@2 ", t_dm%(t)s[0], t_trg_%(wp)s_%(y)s_%(x)s_down%(t)s, t_trg_%(wp)s_%(y)s_%(x)s%(t)s)' % vars())


w.factory('expr::t_eta_bounded("min(2.3,TMath::Abs(@0))" ,t_eta[0])')

# get single tau SF and fit as pol0

f = ROOT.TFile('inputs/SingleTauTrigger/SingleTauTriggerEff_MediumDeepTau2017v2p1_2017_prefit.root')
h1 = f.Get('SF')
func = ROOT.TF1('func','[0]',180,1700)
h1.Fit('func','R')
fit_param = func.GetParameter(0)
fit_param_uncert = func.GetParErrors()[0]

f = ROOT.TFile('inputs/SingleTauTrigger/SingleTauTriggerEff_MediumDeepTau2017v2p1_2017.root')
h1 = f.Get('SF')
func = ROOT.TF1('func','[0]',180,1700)
h1.Fit('func','R')
fit_param_2 = func.GetParameter(0)
fit_param_uncert_2 = func.GetParErrors()[0]
print 'single tau SF:', fit_param, fit_param_uncert
print 'post-fit single tau SF:', fit_param_2, fit_param_uncert_2

uncert = math.sqrt(fit_param_uncert**2 + (fit_param_2-fit_param)**2)

for t in ['','_2']:
  w.factory('expr::t_trg_singletau_medium%(t)s("(@0<180)*0 + (@0>=180)*%(fit_param).5f",t_pt%(t)s[0])' % vars())
  w.factory('expr::t_trg_singletau_medium%(t)s_up("(@0<180)*0 + (@0>=180)*(%(fit_param).5f+%(uncert).5f)",t_pt%(t)s[0])' % vars())
  w.factory('expr::t_trg_singletau_medium%(t)s_down("(@0<180)*0 + (@0>=180)*(%(fit_param).5f-%(uncert).5f)",t_pt%(t)s[0])' % vars())

loc = 'inputs/SingleTauTrigger/trig_effs_2d_2017.root:'

histsToWrap = [
  'embed_sonly',
  'mc_sonly'
]

for task in histsToWrap:
  wsptools.SafeWrapHist(w, ['t_pt'], GetFromTFile(loc+task), name='t_trg_single_'+task.replace('_sonly',''))

uncerts = ['' , '_up', '_down']

for u in uncerts:
  w.factory('expr::t_trg_single_data%(u)s("min(1.,max(@0*@1 ,0.))",t_trg_single_mc, t_trg_singletau_medium%(u)s )' % vars())
  w.factory('expr::t_trg_single_ratio%(u)s("@0/@1",t_trg_single_data%(u)s, t_trg_single_mc)' % vars())
  w.factory('expr::t_trg_single_embed_ratio%(u)s("@0/@1",t_trg_single_data%(u)s, t_trg_single_embed)' % vars())

# make l + tau cross trigger corrections

m_lowpt=25
e_lowpt=28
t_highpt=180
t_lowpt_mt=32
t_lowpt_et=35

for x in ['data','mc','embed','embed_data']:

  x_=x
  if x== 'embed_data': x_='data'

  tau_trig_name = 't_trg_pog_deeptau_medium'
  if 'embed' in x:
    tau_trig_name = 't_trg_mediumDeepTau'

  w.factory('expr::mt_trg_%(x)s("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(m_lowpt)s) + @4*@5*(@0>=%(t_lowpt_mt)s&&@6<2.1&&@1<%(m_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(m_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(m_lowpt)s)) ,0.))",t_pt[0], m_pt[0], t_trg_single_%(x_)s, m_trg_binned_ic_%(x_)s, m_trg_20_binned_ic_%(x_)s, %(tau_trig_name)s_mutau_%(x_)s, t_eta_bounded )' % vars())

  w.factory('expr::et_trg_%(x)s("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(e_lowpt)s) + @4*@5*(@0>=%(t_lowpt_et)s&&@6<2.1&&@1<%(e_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(e_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(e_lowpt)s)) ,0.))",t_pt[0], e_pt[0], t_trg_single_%(x_)s, e_trg_binned_ic_%(x_)s, e_trg_24_binned_ic_%(x_)s, %(tau_trig_name)s_etau_%(x_)s, t_eta_bounded )' % vars())
  
  if 'data' in x:

    for u in ['up', 'down']:
      for i in [0,1,10,11]:

        extra=''
        if 'embed' in x: extra='_embed'

        w.factory('expr::mt_trg_%(x)s_dm%(i)i_%(u)s("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(m_lowpt)s) + @4*@5*@7/@8*(@0>=%(t_lowpt_mt)s&&@6<2.1&&@1<%(m_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(m_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(m_lowpt)s)) ,0.))",t_pt[0], m_pt[0], t_trg_single_%(x_)s, m_trg_binned_ic_%(x_)s, m_trg_20_binned_ic_%(x_)s, %(tau_trig_name)s_mutau_%(x_)s, t_eta_bounded, %(tau_trig_name)s_mutau%(extra)s_ratio_dm%(i)i_%(u)s, %(tau_trig_name)s_mutau%(extra)s_ratio)' % vars())

        w.factory('expr::et_trg_%(x)s_dm%(i)i_%(u)s("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(e_lowpt)s) + @4*@5*@7/@8*(@0>=%(t_lowpt_et)s&&@6<2.1&&@1<%(e_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(e_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(e_lowpt)s)) ,0.))",t_pt[0], e_pt[0], t_trg_single_%(x_)s, e_trg_binned_ic_%(x_)s, e_trg_24_binned_ic_%(x_)s, %(tau_trig_name)s_etau_%(x_)s, t_eta_bounded, %(tau_trig_name)s_etau%(extra)s_ratio_dm%(i)i_%(u)s, %(tau_trig_name)s_etau%(extra)s_ratio )' % vars())

      w.factory('expr::mt_trg_%(x)s_singletau_%(u)s("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(m_lowpt)s) + @4*@5*(@0>=%(t_lowpt_mt)s&&@6<2.1&&@1<%(m_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(m_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(m_lowpt)s)) ,0.))",t_pt[0], m_pt[0], t_trg_single_%(x_)s_%(u)s, m_trg_binned_ic_%(x_)s, m_trg_20_binned_ic_%(x_)s, %(tau_trig_name)s_mutau_%(x_)s, t_eta_bounded )' % vars())

      w.factory('expr::et_trg_%(x)s_singletau_%(u)s("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(e_lowpt)s) + @4*@5*(@0>=%(t_lowpt_et)s&&@6<2.1&&@1<%(e_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(e_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(e_lowpt)s)) ,0.))",t_pt[0], e_pt[0], t_trg_single_%(x_)s_%(u)s, e_trg_binned_ic_%(x_)s, e_trg_24_binned_ic_%(x_)s, %(tau_trig_name)s_etau_%(x_)s, t_eta_bounded )' % vars())

    w.factory('expr::mt_trg_%(x)s_crosslep_up("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(m_lowpt)s) + @4*1.02*@5*(@0>=%(t_lowpt_mt)s&&@6<2.1&&@1<%(m_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(m_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(m_lowpt)s)) ,0.))",t_pt[0], m_pt[0], t_trg_single_%(x_)s, m_trg_binned_ic_%(x_)s, m_trg_20_binned_ic_%(x_)s, %(tau_trig_name)s_mutau_%(x_)s, t_eta_bounded )' % vars())
    w.factory('expr::mt_trg_%(x)s_crosslep_down("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(m_lowpt)s) + @4*0.98*@5*(@0>=%(t_lowpt_mt)s&&@6<2.1&&@1<%(m_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(m_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(m_lowpt)s)) ,0.))",t_pt[0], m_pt[0], t_trg_single_%(x_)s, m_trg_binned_ic_%(x_)s, m_trg_20_binned_ic_%(x_)s, %(tau_trig_name)s_mutau_%(x_)s, t_eta_bounded )' % vars())
    w.factory('expr::mt_trg_%(x)s_singlelep_up("min(1.,max((@0<%(t_highpt)s)*(@3*1.02*(@1>=%(m_lowpt)s) + @4*@5*(@0>=%(t_lowpt_mt)s&&@6<2.1&&@1<%(m_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*1.02*(@1>=%(m_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*1.02*(@1>=%(m_lowpt)s)) ,0.))",t_pt[0], m_pt[0], t_trg_single_%(x_)s, m_trg_binned_ic_%(x_)s, m_trg_20_binned_ic_%(x_)s, %(tau_trig_name)s_mutau_%(x_)s, t_eta_bounded )' % vars())
    w.factory('expr::mt_trg_%(x)s_singlelep_down("min(1.,max((@0<%(t_highpt)s)*(@3*0.98*(@1>=%(m_lowpt)s) + @4*@5*(@0>=%(t_lowpt_mt)s&&@6<2.1&&@1<%(m_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*0.98*(@1>=%(m_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*0.98*(@1>=%(m_lowpt)s)) ,0.))",t_pt[0], m_pt[0], t_trg_single_%(x_)s, m_trg_binned_ic_%(x_)s, m_trg_20_binned_ic_%(x_)s, %(tau_trig_name)s_mutau_%(x_)s, t_eta_bounded )' % vars())

    w.factory('expr::et_trg_%(x)s_crosslep_up("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(e_lowpt)s) + @4*1.02*@5*(@0>=%(t_lowpt_et)s&&@6<2.1&&@1<%(e_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(e_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(e_lowpt)s)) ,0.))",t_pt[0], e_pt[0], t_trg_single_%(x_)s, e_trg_binned_ic_%(x_)s, e_trg_24_binned_ic_%(x_)s, %(tau_trig_name)s_etau_%(x_)s, t_eta_bounded )' % vars())
    w.factory('expr::et_trg_%(x)s_crosslep_down("min(1.,max((@0<%(t_highpt)s)*(@3*(@1>=%(e_lowpt)s) + @4*0.98*@5*(@0>=%(t_lowpt_et)s&&@6<2.1&&@1<%(e_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*(@1>=%(e_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*(@1>=%(e_lowpt)s)) ,0.))",t_pt[0], e_pt[0], t_trg_single_%(x_)s, e_trg_binned_ic_%(x_)s, e_trg_24_binned_ic_%(x_)s, %(tau_trig_name)s_etau_%(x_)s, t_eta_bounded )' % vars())
    w.factory('expr::et_trg_%(x)s_singlelep_up("min(1.,max((@0<%(t_highpt)s)*(@3*1.02*(@1>=%(e_lowpt)s) + @4*@5*(@0>=%(t_lowpt_et)s&&@6<2.1&&@1<%(e_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*1.02*(@1>=%(e_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*1.02*(@1>=%(e_lowpt)s)) ,0.))",t_pt[0], e_pt[0], t_trg_single_%(x_)s, e_trg_binned_ic_%(x_)s, e_trg_24_binned_ic_%(x_)s, %(tau_trig_name)s_etau_%(x_)s, t_eta_bounded )' % vars())
    w.factory('expr::et_trg_%(x)s_singlelep_down("min(1.,max((@0<%(t_highpt)s)*(@3*0.98*(@1>=%(e_lowpt)s) + @4*@5*(@0>=%(t_lowpt_et)s&&@6<2.1&&@1<%(e_lowpt)s)) + (@0>=%(t_highpt)s)*(@2*(@0>=%(t_highpt)s&&@6<2.1) + @3*0.98*(@1>=%(e_lowpt)s) - @2*(@0>=%(t_highpt)s&&@6<2.1)*@3*0.98*(@1>=%(e_lowpt)s)) ,0.))",t_pt[0], e_pt[0], t_trg_single_%(x_)s, e_trg_binned_ic_%(x_)s, e_trg_24_binned_ic_%(x_)s, %(tau_trig_name)s_etau_%(x_)s, t_eta_bounded )' % vars())


systs = ["","_crosslep_up","_crosslep_down","_singlelep_up","_singlelep_down","_singletau_up","_singletau_down","_dm0_up","_dm0_down","_dm1_up","_dm1_down","_dm10_up","_dm10_down","_dm11_up","_dm11_down"]

for u in systs:
  w.factory('expr::mt_trg_ratio%(u)s("(@1>0)*@0/@1 + (@1<=0)*0", mt_trg_data%(u)s, mt_trg_mc)' % vars())
  w.factory('expr::mt_trg_embed_ratio%(u)s("(@1>0)*@0/@1 + (@1<=0)*0", mt_trg_data%(u)s, mt_trg_embed)' % vars())
  w.factory('expr::et_trg_ratio%(u)s("0.991*((@1>0)*@0/@1 + (@1<=0)*0)", et_trg_data%(u)s, et_trg_mc)' % vars())
  w.factory('expr::et_trg_embed_ratio%(u)s("0.991*((@2<40&&fabs(@3)>1.479)*@0 + ((@2<40&&fabs(@3)>1.479)==0)*((@1>0)*@0/@1 + (@1<=0)*0))", et_trg_data%(u)s, et_trg_embed, e_pt[0], e_eta[0])' % vars())

w.Print()
w.writeToFile('output/htt_scalefactors_legacy_trimmed_singletau_ic_2017.root')
w.Delete()
