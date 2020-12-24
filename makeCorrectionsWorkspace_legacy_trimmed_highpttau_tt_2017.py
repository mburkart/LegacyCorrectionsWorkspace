#!/usr/bin/env python
import ROOT
import imp
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

# Tau Tau channel tau trigger weights.

loc = 'inputs/2017/TauPOGTriggerSFs/'
tau_trg_file = ROOT.TFile(loc+'2017_tauTriggerEff_DeepTau2017v2p1.root')
#tau_id_wps=['VVVLoose','VVLoose','VLoose','Loose','Medium','Tight']
tau_id_wps=['Medium']#,'Tight']

for wp in tau_id_wps:
  for dm in ['0','1','10',11]:

    histsToWrap = [
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:data_ditau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_ditau_dm%s_data' % (wp.lower(),dm)),
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:mc_ditau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_ditau_dm%s_mc' % (wp.lower(),dm)),
      (loc+'2017_tauTriggerEff_DeepTau2017v2p1.root:sf_ditau_%s_dm%s_fitted' % (wp,dm),  't_trg_pog_deeptau_%s_ditau_dm%s_ratio' % (wp.lower(),dm)),
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
    for j in ['ditau']:
      taus=['']
      if j == 'ditau': taus = ['', '_2']
      for t in taus:
        w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s("(@0==0)*@1 + (@0==1)*@2 + (@0==10||@0==5)*@3 + (@0==11||@0==6)*@4", t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm0_%(i)s%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm1_%(i)s%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm10_%(i)s%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm11_%(i)s%(t)s)' % vars())

        w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_up%(t)s("@5 + ((@0==0)*@1 + (@0==1)*@2 + (@0==10||@0==5)*@3 + (@0==11||@0==6)*@4)", t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm0_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm1_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm10_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm11_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())

        w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_down%(t)s("@5 - ((@0==0)*@1 + (@0==1)*@2 + (@0==10||@0==5)*@3 + (@0==11||@0==6)*@4)", t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm0_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm1_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm10_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_dm11_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())

        for dm in ['0','1','10','11']:
          w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_dm%(dm)s_down%(t)s("(@0==%(dm)s)*@1 + (@0!=%(dm)s)*@2",t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_down%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())
          w.factory('expr::t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_dm%(dm)s_up%(t)s("(@0==%(dm)s)*@1 + (@0!=%(dm)s)*@2",t_dm%(t)s[0], t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s_up%(t)s, t_trg_pog_deeptau_%(wp_lower)s_%(j)s_%(i)s%(t)s)' % vars())

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

histsToWrap = [
  'embed_nom',
  'embed_d',
  'mc_nom',
  'mc_all',
  'mc_d',
  'mc_d_s2',
  'mc_s2',
  'mc_s1',
  'mc_d_s1',
  'mc_s1_s2',
]

loc = 'inputs/SingleTauTrigger/trig_effs_2d_2017.root:'

for task in histsToWrap:
  print 'loading: ',loc+task 
  wsptools.SafeWrapHist(w, ['t_pt_2','t_pt'], GetFromTFile(loc+task), name='t_trg_2d_'+task.replace('_nom',''))

# split uncerts into low and high pT components
uncerts_dm = ['_dm0_up', '_dm0_down', '_dm1_up', '_dm1_down', '_dm10_up', '_dm10_down', '_dm11_up', '_dm11_down']
for u in uncerts_dm:
  for x in ['','_2']:
    w.factory('expr::t_trg_pog_deeptau_medium_ditau_ratio_highpt%(u)s%(x)s("(@0<100)*@1+(@0>=100)*@2", t_pt%(x)s[0], t_trg_pog_deeptau_medium_ditau_ratio%(x)s, t_trg_pog_deeptau_medium_ditau_ratio%(u)s%(x)s)' % vars())
    w.factory('expr::t_trg_pog_deeptau_medium_ditau_ratio_lowpt%(u)s%(x)s("(@0>=100)*@1+(@0<100)*@2", t_pt%(x)s[0], t_trg_pog_deeptau_medium_ditau_ratio%(x)s, t_trg_pog_deeptau_medium_ditau_ratio%(u)s%(x)s)' % vars())

uncerts = ['' ,
  '_lowpt_dm0_up', '_lowpt_dm0_down', '_lowpt_dm1_up', '_lowpt_dm1_down', '_lowpt_dm10_up', '_lowpt_dm10_down', '_lowpt_dm11_up', '_lowpt_dm11_down',
  '_highpt_dm0_up', '_highpt_dm0_down', '_highpt_dm1_up', '_highpt_dm1_down', '_highpt_dm10_up', '_highpt_dm10_down', '_highpt_dm11_up', '_highpt_dm11_down',
  '_singletau_up', '_singletau_down'
]

for u in uncerts:
  if 'single' in u:
    u_ = u.replace('_singletau','') 
    w.factory('expr::t_trg_2d_data%(u)s("min(1.,max(@0*@7*@8 + @1*@9 + @2*@10  - @3*@8*@9 - @4*@7*@10 - @5*@9*@10 + @6*@9*@10 ,0.))",t_trg_2d_mc_d, t_trg_2d_mc_s1, t_trg_2d_mc_s2, t_trg_2d_mc_d_s1, t_trg_2d_mc_d_s2, t_trg_2d_mc_s1_s2, t_trg_2d_mc_all, t_trg_pog_deeptau_medium_ditau_ratio, t_trg_pog_deeptau_medium_ditau_ratio_2, t_trg_singletau_medium%(u_)s, t_trg_singletau_medium_2%(u_)s )' % vars())
    w.factory('expr::t_trg_2d_data%(u)s_alt1("min(1.,max(@0*@7*@8 + @1*@9 + @2*@10  - @3*@7*@8*@9 - @4*@7*@8*@10 - @5*@9*@10 + @6*@7*@8*@9*@10 ,0.))",t_trg_2d_mc_d, t_trg_2d_mc_s1, t_trg_2d_mc_s2, t_trg_2d_mc_d_s1, t_trg_2d_mc_d_s2, t_trg_2d_mc_s1_s2, t_trg_2d_mc_all, t_trg_pog_deeptau_medium_ditau_ratio, t_trg_pog_deeptau_medium_ditau_ratio_2, t_trg_singletau_medium%(u_)s, t_trg_singletau_medium_2%(u_)s )' % vars())
    w.factory('expr::t_trg_2d_data_d%(u)s("min(1.,max(@0*@1*@2, 0.))",t_trg_2d_mc_d, t_trg_pog_deeptau_medium_ditau_ratio, t_trg_pog_deeptau_medium_ditau_ratio_2)' % vars())
  else:
    w.factory('expr::t_trg_2d_data%(u)s("min(1.,max(@0*@7*@8 + @1*@9 + @2*@10  - @3*@8*@9 - @4*@7*@10 - @5*@9*@10 + @6*@9*@10 ,0.))",t_trg_2d_mc_d, t_trg_2d_mc_s1, t_trg_2d_mc_s2, t_trg_2d_mc_d_s1, t_trg_2d_mc_d_s2, t_trg_2d_mc_s1_s2, t_trg_2d_mc_all, t_trg_pog_deeptau_medium_ditau_ratio%(u)s, t_trg_pog_deeptau_medium_ditau_ratio%(u)s_2, t_trg_singletau_medium, t_trg_singletau_medium_2 )' % vars())

    w.factory('expr::t_trg_2d_data_d%(u)s("min(1.,max(@0*@1*@2, 0.))",t_trg_2d_mc_d, t_trg_pog_deeptau_medium_ditau_ratio%(u)s, t_trg_pog_deeptau_medium_ditau_ratio%(u)s_2)' % vars())

  w.factory('expr::t_trg_2d_ratio%(u)s("@0/@1",t_trg_2d_data%(u)s, t_trg_2d_mc)' % vars())
  w.factory('expr::t_trg_2d_embed_ratio%(u)s("@0/@1",t_trg_2d_data%(u)s, t_trg_2d_embed)' % vars())

  w.factory('expr::t_trg_2d_doubleonly_ratio%(u)s("@0/@1",t_trg_2d_data_d%(u)s, t_trg_2d_mc_d)' % vars())
  w.factory('expr::t_trg_2d_doubleonly_embed_ratio%(u)s("@0/@1",t_trg_2d_data_d%(u)s, t_trg_2d_embed_d)' % vars())

w.Print()
w.writeToFile('output/htt_scalefactors_legacy_trimmed_highpttau_tt_2017.root')
w.Delete()
