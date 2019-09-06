import ROOT

def getConfidenceInterval(g_efficiency, histo, graph, CL): # give CL as 0.68 or 0.95

        TVirtualFitter.GetFitter().GetConfidenceIntervals(histo, CL)

        for i in range(0, g_efficiency.GetN()):
                graph.SetPoint(i, g_efficiency.GetX()[i], 0)
                TVirtualFitter.GetFitter().GetConfidenceIntervals(graph, CL)

        return histo, graph

draw_hists=True
loc = 'inputs/2018/KIT/TauTrigger/'

infile = ROOT.TFile(loc+'/output_2018_tau_leg.root')
fout = ROOT.TFile(loc+'/tau_trigger_fits.root','RECREATE')

samples = ['EMB', 'DATA']
tau_id_wps=['vloose','loose','medium','tight','vtight']

channels = ['ditau', 'mutau', 'etau']

c = ROOT.TCanvas()
#c.SetLogx(1)

pars_map = {}
pars_map['etau_dm0']  = [0.8,10.,5.,-25.,1.,1.]
pars_map['etau_dm10'] = [0.3,5.,3,-30,0.95,0.95]
pars_map['etau_dm1']  = [0.7,3.,3.,-30.,0.9,0.9]

pars_map['mutau_dm0'] = [0.5,5.0,7.0,-20.,1.0,1.0] 
pars_map['mutau_dm1'] = [0.8,2.0,2.0,-30.,0.9,0.95]
pars_map['mutau_dm10'] = [0.8,10.,0.2,-25.,1.,1.] 

pars_map['mutau_dm0_embed'] = [1.,2.,1.,-15.,1.0,1.0]
pars_map['mutau_dm1_embed'] = [2.,5.,5.,-10.,1.,1.0]
pars_map['mutau_dm10_embed'] = [1.,120.,7.,-25.,1.,1.]

pars_map['etau_dm0_embed'] = [0.5,5.0,7.0,-20.,1.0,1.0]
pars_map['etau_dm1_embed'] = [0.5,5.0,7.0,-20.,1.0,1.0]
pars_map['etau_dm10_embed'] = [0.1,40.,1.5,-25.,1.,1.]

pars_map['ditau_dm0_embed'] = [1.0,2.0,5.,-40.,1.,1.]
pars_map['ditau_dm1_embed'] = [1.0,2.0,5.,-40.,1.,1.]
pars_map['ditau_dm10_embed'] = [1.0,2.,5.,-40.,1.,1.]

pars_map['ditau_dm10'] = [0.1,100.,2.,-35.,0.95,0.95] 
pars_map['ditau_dm1'] = [0.8,4.,5.,-40.,0.9,0.9]
pars_map['ditau_dm0'] = [0.5,125,5.,-35.,0.8,0.8]


for chan in channels:
  for wp in tau_id_wps:
    for s in samples:
      g_dm0 = infile.Get('graph_%sTriggerEfficiency_%sTauMVA_dm0_%s' % (chan, wp, s))
      g_dm1 = infile.Get('graph_%sTriggerEfficiency_%sTauMVA_dm1_%s' % (chan, wp, s))
      g_dm10 = infile.Get('graph_%sTriggerEfficiency_%sTauMVA_dm10_%s' % (chan, wp, s))
      fit = ROOT.TF1('fit', '[5] - ROOT::Math::crystalball_cdf(-x, [0], [1], [2], [3])*([4])',20,400)

      fit_dm0 = fit.Clone(); fit_dm0.SetName('fit_%s_%s_dm0_%s' % (chan, wp, s))
      fit_dm1 = fit.Clone(); fit_dm1.SetName('fit_%s_%s_dm1_%s' % (chan, wp, s))
      fit_dm10 = fit.Clone(); fit_dm10.SetName('fit_%s_%s_dm10_%s' % (chan, wp, s))
     
      extra=''
      if s == 'EMB': extra = '_embed'
      for i, p in enumerate(pars_map['%s_dm0%s' % (chan,extra)]): fit_dm0.SetParameter(i,p)
      for i, p in enumerate(pars_map['%s_dm1%s' % (chan,extra)]): fit_dm1.SetParameter(i,p)
      for i, p in enumerate(pars_map['%s_dm10%s' % (chan,extra)]): fit_dm10.SetParameter(i,p)

      hist_map = {'dm0': [g_dm0,fit_dm0], 'dm1': [g_dm1,fit_dm1], 'dm10': [g_dm10,fit_dm10]}  

      for i in hist_map:
        f = hist_map[i][0]
        name = '%s_%s_%s_%s' % (chan, wp, i, s)
        f.Fit('fit_%s' %name, 'r')
        fout.cd()
        f.Write(name)
        hist_map[i][1].Write('fit_'+name)

        #if draw_hists:
        #  name = '%s_%s_%s_%s' % (chan, wp, i, s)
        #  f.GetXaxis().SetRangeUser(0,400)
        #  f.SetTitle(name) 
        #  f.GetXaxis().SetTitle('p_{T} (GeV)')
        #  f.Draw('ap')
        #  c.Print('%s_fit.pdf' % (name))

if draw_hists:
  for chan in channels:
    for wp in tau_id_wps:
      for i in ['0','1','10']:
        name_data = '%s_%s_dm%s_DATA' % (chan, wp, i)
        name_embed = '%s_%s_dm%s_EMB' % (chan, wp, i)
        name = '%s_%s_dm%s' % (chan, wp, i)
        f1 = fout.Get(name_data)
        f2 = fout.Get(name_embed)
        f1.GetFunction('fit_'+name_data).SetLineColor(f1.GetLineColor())
        f2.SetLineColor(ROOT.kRed)
        f2.GetFunction('fit_'+name_embed).SetLineColor(ROOT.kRed)
        f1.GetXaxis().SetRangeUser(0,400)
        f1.SetMaximum(1.1)
        f1.SetTitle(name)
        f1.GetXaxis().SetTitle('p_{T} (GeV)')
        f1.Draw('ap')
        f2.Draw('p same')
        c.Print('%s_fit.pdf' % (name))
        
      
