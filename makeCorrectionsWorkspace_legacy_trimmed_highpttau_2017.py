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

# differential tau ID SFs from tau POG

# dm binned SFs

loc='inputs/2017/TauPOGIDSFs/'

# pT dependent SFs

sf_funcs = {}

# sf_funcs['vloose'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.7680031+ ( x > 25 && x <=30)*0.8770162+ ( x > 30 && x <=35)*0.8864078+ ( x > 35 && x <=40)*0.8575877+ (x > 40)*0.908802967687'
# sf_funcs['vloose_up'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.8890281+ ( x > 25 && x <=30)*0.9469252+ ( x > 30 && x <=35)*0.9380708+ ( x > 35 && x <=40)*0.9044377+ (x > 40 && x <= 500)*0.949084749706+ (x > 500 && x <= 1000)*(0.908802967687 +0.0402817820196*(x/500.))+ (x > 1000)*(0.908802967687 + 0.0805635640393)'
# sf_funcs['vloose_down'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.6469781+ ( x > 25 && x <=30)*0.8071072+ ( x > 30 && x <=35)*0.8347448+ ( x > 35 && x <=40)*0.8107377+ (x > 40 && x <= 500)*0.861070663387+ (x > 500 && x <= 1000)*(0.908802967687 -0.0477323042994*(x/500.))+ (x > 1000)*(0.908802967687 - 0.0954646085989)'
# sf_funcs['loose'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.8666298+ ( x > 25 && x <=30)*0.8612201+ ( x > 30 && x <=35)*0.8722173+ ( x > 35 && x <=40)*0.8877534+ (x > 40)*0.94820719806'
# sf_funcs['loose_up'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.9511748+ ( x > 25 && x <=30)*0.9251961+ ( x > 30 && x <=35)*0.9088133+ ( x > 35 && x <=40)*0.9270814+ (x > 40 && x <= 500)*0.986524358469+ (x > 500 && x <= 1000)*(0.94820719806 +0.0383171604096*(x/500.))+ (x > 1000)*(0.94820719806 + 0.0766343208191)'
# sf_funcs['loose_down'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.7820848+ ( x > 25 && x <=30)*0.7972441+ ( x > 30 && x <=35)*0.8356213+ ( x > 35 && x <=40)*0.8484254+ (x > 40 && x <= 500)*0.899402790402+ (x > 500 && x <= 1000)*(0.94820719806 -0.0488044076576*(x/500.))+ (x > 1000)*(0.94820719806 - 0.0976088153153)'
sf_funcs['medium'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.91902+ ( x > 25 && x <=30)*0.8435835+ ( x > 30 && x <=35)*0.8852934+ ( x > 35 && x <=40)*0.8848557+ (x > 40)*0.906817421521'
sf_funcs['medium_up'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.984677+ ( x > 25 && x <=30)*0.8896395+ ( x > 30 && x <=35)*0.9164874+ ( x > 35 && x <=40)*0.9181077+ (x > 40 && x <= 500)*0.951709411669+ (x > 500 && x <= 1000)*(0.906817421521 +0.0448919901481*(x/500.))+ (x > 1000)*(0.906817421521 + 0.0897839802962)'
sf_funcs['medium_down'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.853363+ ( x > 25 && x <=30)*0.7975275+ ( x > 30 && x <=35)*0.8540994+ ( x > 35 && x <=40)*0.8516037+ (x > 40 && x <= 500)*0.860601947029+ (x > 500 && x <= 1000)*(0.906817421521 -0.0462154744917*(x/500.))+ (x > 1000)*(0.906817421521 - 0.0924309489835)'
# sf_funcs['tight'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.9368875+ ( x > 25 && x <=30)*0.8456867+ ( x > 30 && x <=35)*0.8688679+ ( x > 35 && x <=40)*0.8719202+ (x > 40)*0.8984880855'
# sf_funcs['tight_up'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.9935635+ ( x > 25 && x <=30)*0.8866707+ ( x > 30 && x <=35)*0.8973459+ ( x > 35 && x <=40)*0.9072442+ (x > 40 && x <= 500)*0.935249492999+ (x > 500 && x <= 1000)*(0.8984880855 +0.0367614074987*(x/500.))+ (x > 1000)*(0.8984880855 + 0.0735228149975)'
# sf_funcs['tight_down'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.8802115+ ( x > 25 && x <=30)*0.8047027+ ( x > 30 && x <=35)*0.8403899+ ( x > 35 && x <=40)*0.8365962+ (x > 40 && x <= 500)*0.859400181792+ (x > 500 && x <= 1000)*(0.8984880855 -0.0390879037079*(x/500.))+ (x > 1000)*(0.8984880855 - 0.0781758074157)'
# sf_funcs['vtight'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.9230896+ ( x > 25 && x <=30)*0.8675593+ ( x > 30 && x <=35)*0.8532677+ ( x > 35 && x <=40)*0.8516027+ (x > 40)*0.861147095013'
# sf_funcs['VTight_up'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.9710176+ ( x > 25 && x <=30)*0.8988653+ ( x > 30 && x <=35)*0.8781697+ ( x > 35 && x <=40)*0.8848917+ (x > 40 && x <= 500)*0.900692367516+ (x > 500 && x <= 1000)*(0.861147095013 +0.0395452725033*(x/500.))+ (x > 1000)*(0.861147095013 + 0.0790905450065)'
# sf_funcs['vtight_down'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.8751616+ ( x > 25 && x <=30)*0.8362533+ ( x > 30 && x <=35)*0.8283657+ ( x > 35 && x <=40)*0.8183137+ (x > 40 && x <= 500)*0.821314916483+ (x > 500 && x <= 1000)*(0.861147095013 -0.0398321785294*(x/500.))+ (x > 1000)*(0.861147095013 - 0.0796643570588)'
# sf_funcs['vvtight'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.8824266+ ( x > 25 && x <=30)*0.8587208+ ( x > 30 && x <=35)*0.8414515+ ( x > 35 && x <=40)*0.8518679+ (x > 40)*0.87882485674'
# sf_funcs['vvtight_up'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.9222017+ ( x > 25 && x <=30)*0.8868838+ ( x > 30 && x <=35)*0.8645885+ ( x > 35 && x <=40)*0.9197789+ (x > 40 && x <= 500)*0.926167548222+ (x > 500 && x <= 1000)*(0.87882485674 +0.0473426914828*(x/500.))+ (x > 1000)*(0.87882485674 + 0.0946853829656)'
# sf_funcs['vvtight_down'] = '(x<=20)*0+ ( x > 20 && x <=25)*0.8426516+ ( x > 25 && x <=30)*0.8305578+ ( x > 30 && x <=35)*0.8183145+ ( x > 35 && x <=40)*0.7839569+ (x > 40 && x <= 500)*0.829600880712+ (x > 500 && x <= 1000)*(0.87882485674 -0.049223976028*(x/500.))+ (x > 1000)*(0.87882485674 - 0.098447952056)'

import re
for x in sf_funcs:
  func = re.sub('x','@0',sf_funcs[x])
  w.factory('expr::t_id_pt_%s("%s",t_pt[0])' % (x, func))

# PRELIMINARY differential tau ID SFs for deepTau ID from Yuta

# dm binned SFs

loc='inputs/2017/TauPOGIDSFs/'

histsToWrap = [
  (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:VVVLoose', 't_deeptauid_dm_vvvloose'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:VVLoose',  't_deeptauid_dm_vvloose'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:VLoose',   't_deeptauid_dm_vloose'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:Loose',    't_deeptauid_dm_loose'),
  (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:Medium',   't_deeptauid_dm_medium'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:Tight',    't_deeptauid_dm_tight'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:VTight',   't_deeptauid_dm_vtight'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco.root:VVTight',  't_deeptauid_dm_vvtight'),
  (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:VVVLoose', 't_deeptauid_dm_embed_vvvloose'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:VVLoose',  't_deeptauid_dm_embed_vvloose'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:VLoose',   't_deeptauid_dm_embed_vloose'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:Loose',    't_deeptauid_dm_embed_loose'),
  (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:Medium',   't_deeptauid_dm_embed_medium'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:Tight',    't_deeptauid_dm_embed_tight'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:VTight',   't_deeptauid_dm_embed_vtight'),
  # (loc+'/TauID_SF_dm_DeepTau2017v2p1VSjet_2017ReReco_EMB.root:VVTight',  't_deeptauid_dm_embed_vvtight')
]

for task in histsToWrap:
  wsptools.SafeWrapHist(w, ['t_dm_bounded'], GetFromTFile(task[0]), name=task[1])
  uncert_hists = wsptools.UncertsFromHist(GetFromTFile(task[0]))
  wsptools.SafeWrapHist(w, ['t_dm_bounded'], uncert_hists[0], name=task[1]+'_abs_up')
  wsptools.SafeWrapHist(w, ['t_dm_bounded'], uncert_hists[1], name=task[1]+'_abs_down')
  w.factory('expr::%s_up("@1+@0",%s_abs_up,%s)' % (task[1],task[1],task[1]))
  w.factory('expr::%s_down("@1-@0",%s_abs_down,%s)' % (task[1],task[1],task[1]))

  w.factory('expr::%s_dm0_up("(@0==0)*@1 + (@0!=0)*@2 ", t_dm[0], %s_up, %s)' % (task[1],task[1],task[1]))
  w.factory('expr::%s_dm0_down("(@0==0)*@1 + (@0!=0)*@2 ", t_dm[0], %s_down, %s)' % (task[1],task[1],task[1]))

  w.factory('expr::%s_dm1_up("(@0==1)*@1 + (@0!=1)*@2 ", t_dm[0], %s_up, %s)' % (task[1],task[1],task[1]))
  w.factory('expr::%s_dm1_down("(@0==1)*@1 + (@0!=1)*@2 ", t_dm[0], %s_down, %s)' % (task[1],task[1],task[1]))

  w.factory('expr::%s_dm10_up("(@0==10)*@1 + (@0!=10)*@2 ", t_dm[0], %s_up, %s)' % (task[1],task[1],task[1]))
  w.factory('expr::%s_dm10_down("(@0==10)*@1 + (@0!=10)*@2 ", t_dm[0], %s_down, %s)' % (task[1],task[1],task[1]))

  w.factory('expr::%s_dm11_up("(@0==11)*@1 + (@0!=11)*@2 ", t_dm[0], %s_up, %s)' % (task[1],task[1],task[1]))
  w.factory('expr::%s_dm11_down("(@0==11)*@1 + (@0!=11)*@2 ", t_dm[0], %s_down, %s)' % (task[1],task[1],task[1]))

# pT dependent SFs

sf_funcs = {}

sf_funcs = {}
tauid_pt_file = ROOT.TFile(loc+'/TauID_SF_pt_DeepTau2017v2p1VSjet_2017ReReco.root')
# for i in ['VVVLoose', 'VVLoose', 'VLoose', 'Loose', 'Medium', 'Tight', 'VTight', 'VVTight']:
for i in ['VVVLoose', 'Medium']:
  for j in ['cent', 'up', 'down']:
    fname = '%s_%s' % (i,j)
    fit = tauid_pt_file.Get(fname)
    outname = i.lower()
    if j != 'cent': outname+='_%s' % j
    sf_funcs[outname] = fit.GetTitle()


for x in sf_funcs:
  func = re.sub('x','@0',sf_funcs[x])
  w.factory('expr::t_deeptauid_pt_%s("%s",t_pt[0])' % (x, func))

# for i in ['vvvloose', 'vvloose', 'vloose', 'loose', 'medium', 'tight', 'vtight', 'vvtight']:
for i in ['vvvloose', 'medium']:
  # w.factory('expr::t_deeptauid_pt_%(i)s_bin1_up("(@0>20&&@0<=25)*@1 + ((@0>20&&@0<=25)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_up, t_deeptauid_pt_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_%(i)s_bin1_down("(@0>20&&@0<=25)*@1 + ((@0>20&&@0<=25)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_down, t_deeptauid_pt_%(i)s)' % vars())

  # w.factory('expr::t_deeptauid_pt_%(i)s_bin2_up("(@0>25&&@0<=30)*@1 + ((@0>25&&@0<=30)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_up, t_deeptauid_pt_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_%(i)s_bin2_down("(@0>25&&@0<=30)*@1 + ((@0>25&&@0<=30)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_down, t_deeptauid_pt_%(i)s)' % vars())

  # w.factory('expr::t_deeptauid_pt_%(i)s_bin3_up("(@0>30&&@0<=35)*@1 + ((@0>30&&@0<=35)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_up, t_deeptauid_pt_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_%(i)s_bin3_down("(@0>30&&@0<=35)*@1 + ((@0>30&&@0<=35)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_down, t_deeptauid_pt_%(i)s)' % vars())

  # w.factory('expr::t_deeptauid_pt_%(i)s_bin4_up("(@0>35&&@0<=40)*@1 + ((@0>35&&@0<=40)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_up, t_deeptauid_pt_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_%(i)s_bin4_down("(@0>35&&@0<=40)*@1 + ((@0>35&&@0<=40)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_down, t_deeptauid_pt_%(i)s)' % vars())

  w.factory('expr::t_deeptauid_pt_%(i)s_bin5_up("(@0>40&&@0<=500)*@1 + ((@0>40&&@0<=500)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_up, t_deeptauid_pt_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_%(i)s_bin5_down("(@0>40&&@0<=500)*@1 + ((@0>40&&@0<=500)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_down, t_deeptauid_pt_%(i)s)' % vars())

  #w.factory('expr::t_deeptauid_pt_%(i)s_bin5_up("(@0>40)*@1 + ((@0>40)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_up, t_deeptauid_pt_%(i)s)' % vars())
  #w.factory('expr::t_deeptauid_pt_%(i)s_bin5_down("(@0>40)*@1 + ((@0>40)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_down, t_deeptauid_pt_%(i)s)' % vars())

  w.factory('expr::t_deeptauid_pt_%(i)s_bin6_up("(@0>500)*@1 + ((@0>500)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_up, t_deeptauid_pt_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_%(i)s_bin6_down("(@0>500)*@1 + ((@0>500)==0)*@2",t_pt[0], t_deeptauid_pt_%(i)s_down, t_deeptauid_pt_%(i)s)' % vars())

  w.factory('expr::t_deeptauid_dm_%(i)s_bin6_up("((@0>500)*@1/@2 + ((@0>500)==0))*@3",t_pt[0], t_deeptauid_pt_%(i)s_bin6_up, t_deeptauid_pt_%(i)s, t_deeptauid_dm_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_dm_%(i)s_bin6_down("((@0>500)*@1/@2 + ((@0>500)==0))*@3",t_pt[0], t_deeptauid_pt_%(i)s_bin6_down, t_deeptauid_pt_%(i)s, t_deeptauid_dm_%(i)s)' % vars())

# embedded SFs

sf_funcs = {}

sf_funcs = {}
tauid_pt_file = ROOT.TFile(loc+'/TauID_SF_pt_DeepTau2017v2p1VSjet_2017ReReco_EMB.root')
# for i in ['VVVLoose', 'VVLoose', 'VLoose', 'Loose', 'Medium', 'Tight', 'VTight', 'VVTight']:
for i in ['VVVLoose', 'Medium']:
  for j in ['cent', 'up', 'down']:
    fname = '%s_%s' % (i,j)
    fit = tauid_pt_file.Get(fname)
    outname = i.lower()
    if j != 'cent': outname+='_%s' % j
    sf_funcs[outname] = fit.GetTitle()


for x in sf_funcs:
  func = re.sub('x','@0',sf_funcs[x])
  w.factory('expr::t_deeptauid_pt_embed_%s("%s",t_pt[0])' % (x, func))

# for i in ['vvvloose', 'vvloose', 'vloose', 'loose', 'medium', 'tight', 'vtight', 'vvtight']:
for i in ['vvvloose', 'medium']:
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin1_up("(@0>20&&@0<=25)*@1 + ((@0>20&&@0<=25)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_up, t_deeptauid_pt_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin1_down("(@0>20&&@0<=25)*@1 + ((@0>20&&@0<=25)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_down, t_deeptauid_pt_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin2_up("(@0>25&&@0<=30)*@1 + ((@0>25&&@0<=30)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_up, t_deeptauid_pt_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin2_down("(@0>25&&@0<=30)*@1 + ((@0>25&&@0<=30)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_down, t_deeptauid_pt_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin3_up("(@0>30&&@0<=35)*@1 + ((@0>30&&@0<=35)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_up, t_deeptauid_pt_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin3_down("(@0>30&&@0<=35)*@1 + ((@0>30&&@0<=35)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_down, t_deeptauid_pt_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin4_up("(@0>35&&@0<=40)*@1 + ((@0>35&&@0<=40)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_up, t_deeptauid_pt_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin4_down("(@0>35&&@0<=40)*@1 + ((@0>35&&@0<=40)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_down, t_deeptauid_pt_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin5_up("(@0>40&&@0<=500)*@1 + ((@0>40&&@0<=500)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_up, t_deeptauid_pt_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin5_down("(@0>40&&@0<=500)*@1 + ((@0>40&&@0<=500)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_down, t_deeptauid_pt_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin6_up("(@0>500)*@1 + ((@0>500)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_up, t_deeptauid_pt_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_embed_%(i)s_bin6_down("(@0>500)*@1 + ((@0>500)==0)*@2",t_pt[0], t_deeptauid_pt_embed_%(i)s_down, t_deeptauid_pt_embed_%(i)s)' % vars())

  w.factory('expr::t_deeptauid_dm_embed_%(i)s_bin6_up("((@0>500)*@1/@2 + ((@0>500)==0))*@3",t_pt[0], t_deeptauid_pt_embed_%(i)s_bin6_up, t_deeptauid_pt_embed_%(i)s, t_deeptauid_dm_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_dm_embed_%(i)s_bin6_down("((@0>500)*@1/@2 + ((@0>500)==0))*@3",t_pt[0], t_deeptauid_pt_embed_%(i)s_bin6_down, t_deeptauid_pt_embed_%(i)s, t_deeptauid_dm_embed_%(i)s)' % vars())

# extra SFs for tight anti-electron ID
sf_funcs = {}
tauid_pt_file = ROOT.TFile(loc+'/TauID_SF_pt_DeepTau2017v2p1VSjet_2017ReReco_tight_antie_EMB.root')
# for i in ['VVVLoose', 'VVLoose', 'VLoose', 'Loose', 'Medium', 'Tight', 'VTight', 'VVTight']:
for i in ["VVVLoose", "Medium"]:
  for j in ['cent', 'up', 'down']:
    fname = '%s_%s' % (i,j)
    fit = tauid_pt_file.Get(fname)
    outname = i.lower()
    if j != 'cent': outname+='_%s' % j
    sf_funcs[outname] = fit.GetTitle()


for x in sf_funcs:
  func = re.sub('x','@0',sf_funcs[x])
  w.factory('expr::t_deeptauid_pt_tightvse_embed_%s("%s",t_pt[0])' % (x, func))

# for i in ['vvvloose', 'vvloose', 'vloose', 'loose', 'medium', 'tight', 'vtight', 'vvtight']:
for i in ['vvvloose', 'medium']:
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin1_up("(@0>20&&@0<=25)*@1 + ((@0>20&&@0<=25)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_up, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin1_down("(@0>20&&@0<=25)*@1 + ((@0>20&&@0<=25)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_down, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin2_up("(@0>25&&@0<=30)*@1 + ((@0>25&&@0<=30)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_up, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin2_down("(@0>25&&@0<=30)*@1 + ((@0>25&&@0<=30)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_down, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin3_up("(@0>30&&@0<=35)*@1 + ((@0>30&&@0<=35)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_up, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin3_down("(@0>30&&@0<=35)*@1 + ((@0>30&&@0<=35)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_down, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin4_up("(@0>35&&@0<=40)*@1 + ((@0>35&&@0<=40)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_up, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  # w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin4_down("(@0>35&&@0<=40)*@1 + ((@0>35&&@0<=40)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_down, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin5_up("(@0>40&&@0<=500)*@1 + ((@0>40&&@0<=500)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_up, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin5_down("(@0>40&&@0<=500)*@1 + ((@0>40&&@0<=500)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_down, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())

  w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin6_up("(@0>500)*@1 + ((@0>500)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_up, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())
  w.factory('expr::t_deeptauid_pt_tightvse_embed_%(i)s_bin6_down("(@0>500)*@1 + ((@0>500)==0)*@2",t_pt[0], t_deeptauid_pt_tightvse_embed_%(i)s_down, t_deeptauid_pt_tightvse_embed_%(i)s)' % vars())


w.factory('expr::t_eta_bounded("min(2.3,TMath::Abs(@0))" ,t_eta[0])')

# high pT tau ID scale factors and uncertainties (from AN-19-263)
# 2017:
tau_id_sf = {
  'pt100to200': (0.71, 0.71+0.11, 0.71-0.12),
  'ptgt200': (0.76, 0.76+0.12, 0.76-0.11)
}

# w.factory('expr::t_deeptauid_highpt_binned("(@0>=100&&@0<200)*%.5f + (@0>=200)*%.5f",t_pt[0])' % (tau_id_sf['pt100to200'][0], tau_id_sf['ptgt200'][0]))
# w.factory('expr::t_deeptauid_highpt_binned_bin1_up("(@0>=100&&@0<200)*%.5f + (@0>=200)*%.5f",t_pt[0])' % (tau_id_sf['pt100to200'][1], tau_id_sf['ptgt200'][0]))
# w.factory('expr::t_deeptauid_highpt_binned_bin1_down("(@0>=100&&@0<200)*%.5f + (@0>=200)*%.5f",t_pt[0])' % (tau_id_sf['pt100to200'][2], tau_id_sf['ptgt200'][0]))
# w.factory('expr::t_deeptauid_highpt_binned_bin2_up("(@0>=100&&@0<200)*%.5f + (@0>=200)*%.5f",t_pt[0])' % (tau_id_sf['pt100to200'][0], tau_id_sf['ptgt200'][1]))
# w.factory('expr::t_deeptauid_highpt_binned_bin2_down("(@0>=100&&@0<200)*%.5f + (@0>=200)*%.5f",t_pt[0])' % (tau_id_sf['pt100to200'][0], tau_id_sf['ptgt200'][2]))

w.factory('expr::t_deeptauid_highpt("@0",t_deeptauid_pt_medium)')
w.factory('expr::t_deeptauid_highpt_bin5_up("@0",t_deeptauid_pt_medium_bin5_up)')
w.factory('expr::t_deeptauid_highpt_bin5_down("@0",t_deeptauid_pt_medium_bin5_down)')
w.factory('expr::t_deeptauid_highpt_bin6_up("@0",t_deeptauid_pt_medium_bin6_up)')
w.factory('expr::t_deeptauid_highpt_bin6_down("@0",t_deeptauid_pt_medium_bin6_down)')

f = ROOT.TFile('inputs/TauIDHighPT/tau_id_comps_2017.root')
func1 = ROOT.TF1('func1','[0]',100,200)
func2 = ROOT.TF1('func2','[0]',100,200)
func1_1 = ROOT.TF1('func1_1','[0]',200,400)
func2_1 = ROOT.TF1('func2_1','[0]',200,400)
h1 = f.Get('sf_tt')
h2 = f.Get('sf_et')
h1.Fit('func1','R')
h2.Fit('func2','R')
fit_param1 = func1.GetParameter(0)
fit_param2 = func2.GetParameter(0)

h1.Fit('func1_1','R')
h2.Fit('func2_1','R')
fit_param1_1 = func1_1.GetParameter(0)
fit_param2_1 = func2_1.GetParameter(0)

# for i in ['', '_bin1_up', '_bin1_down', '_bin2_up', '_bin2_down']:
#   w.factory('expr::t_deeptauid_highpt_binned_embed%(i)s("@0*(%(fit_param1).5f*(@1<200)+%(fit_param1_1).5f*(@1>=200))", t_deeptauid_highpt_binned%(i)s, t_pt[0])' % vars())
#   w.factory('expr::t_deeptauid_highpt_binned_tightvse_embed%(i)s("@0*(%(fit_param2).5f*(@1<200)+%(fit_param2_1).5f*(@1>=200))", t_deeptauid_highpt_binned%(i)s, t_pt[0])' % vars())

for i in ['', '_bin5_up', '_bin5_down', '_bin6_up', '_bin6_down']:
  w.factory('expr::t_deeptauid_highpt_embed%(i)s("@0*(%(fit_param1).5f*(@1<200)+%(fit_param1_1).5f*(@1>=200))", t_deeptauid_highpt%(i)s, t_pt[0])' % vars())
  w.factory('expr::t_deeptauid_highpt_tightvse_embed%(i)s("@0*(%(fit_param2).5f*(@1<200)+%(fit_param2_1).5f*(@1>=200))", t_deeptauid_highpt%(i)s, t_pt[0])' % vars())

w.Print()
w.writeToFile('output/htt_scalefactors_legacy_trimmed_highpttau_2017.root')
w.Delete()
