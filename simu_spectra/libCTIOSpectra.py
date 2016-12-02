"""
libCTIOSpectra.py
=============----


author : Sylvie Dagoret-Campagne
affiliation : LAL/CNRS/IN2P3/FRANCE
Collaboration : DESC-LSST


Purpose : study of atmosphere of CTIO

"""


import os
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.io import ascii
import os
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import interp1d

#---------------------------------------------------------------------------------
# DATA BLOCK 

#
filepath_qe='../Telescope'
filename_qe = "qecurve.txt"  

filepath_sed='/Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOData2016/SEDCalspec_HD14943'
filename_sed='hd14943_stis_003.fits'


filepath_atm="/Users/dagoret-campagnesylvie/MacOsX/LSST/MyWork/GitHub/CTIOAna2016/atmosphere/simulations/RT/2.0/CT/pp/us/sa/rt/y2016/m10/out"
filename_atm="RT_CT_pp_us_sa_rt_HD14943_Nev1_y2016_m10_aver.OUT"
#-------------------------------------------------------------------------------


#-----------------------------------------------------------------------------
def Get_QE(filename):
   
    data_qe=ascii.read(filename) 
    x=data_qe["col1"]
    y=data_qe["col2"]/100.
    indexes = np.where(np.logical_and(x>250.,x<1200.)) 
    return x[indexes],y[indexes]  
#------------------------------------------------------------------------------
def Get_Atm(filename):
    data = np.loadtxt(filename)
    x=data[:,0]
    y=data[:,1]
    indexes = np.where(np.logical_and(x>250.,x<1200.)) 
    return x[indexes],y[indexes]    
#-----------------------------------------------------------------------------

def Get_SED(filename):
    hdulist=fits.open(filename)
    table_data=hdulist[1].data
    wavelengths=table_data.field('WAVELENGTH')/10.
    
    indexes = np.where(np.logical_and( wavelengths>300.,wavelengths<1100.))    
    fluxes=table_data.field('FLUX')
    return wavelengths[indexes],fluxes[indexes]
#-------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
def ComputeSEDxAtmxQE(wl_sed,sed,wl_atm,atm,wl_qe,qe):
    interpol_atm=interp1d(wl_atm,atm)
    interpol_qe=interp1d(wl_qe,qe)
    return sed*interpol_atm(wl_sed)*interpol_qe(wl_sed)*wl_sed 

#------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
def ComputeAtm(wl_sed,wl_atm,atm):
    interpol_atm=interp1d(wl_atm,atm)
    return interpol_atm(wl_sed)

#------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
def ComputeQE(wl_sed,wl_qe,qe):
    interpol_qe=interp1d(wl_qe,qe)
    return interpol_qe(wl_sed)

#------------------------------------------------------------------------------



#---------------------------------------------------------------
def PlotQE():
    filename=os.path.join(filepath_qe,filename_qe)    
    wl,qe=Get_QE(filename)
  
    plt.figure()
    plt.plot(wl,qe,"-")
    plt.title('Quantum efficiency')
    plt.xlabel("$\lambda$")
    plt.ylabel("QE")
    
#----------------------------------------------------------------------------------    
def PlotSED():
    
    
    filename=os.path.join(filepath_sed,filename_sed)    
    wl,sed=Get_SED(filename)
    
    print wl.shape
    plt.figure()
    plt.plot(wl,sed,'-')
    plt.title('SED')
    
    plt.xlabel('$\lambda$ (nm)')
    plt.ylabel('sed')
    
#------------------------------------------------------------
def PlotAtmosphere():
    filename=os.path.join(filepath_atm,filename_atm)    
    wl,tr=Get_Atm(filename)
    
    plt.figure()
    plt.plot(wl,tr)
    plt.title('atmosphere')
    plt.xlabel('$\lambda$ (nm)')
    plt.ylabel('atmosphere transmission')
    plt.xlim(300,1100)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
if __name__ == "__main__":

    # 1) Example of SED
    # -------------------
    PlotSED()

    PlotQE()
    
    PlotAtmosphere()
    
    filename=os.path.join(filepath_sed,filename_sed)    
    wl_sed,sed=Get_SED(filename)
   
    filename=os.path.join(filepath_qe,filename_qe)    
    wl_qe,qe=Get_QE(filename)

    filename=os.path.join(filepath_atm,filename_atm)    
    wl_atm,atm=Get_Atm(filename)
    
    spectra=ComputeSEDxAtmxQE(wl_sed,sed,wl_atm,atm,wl_qe,qe)
    plt.figure()
    plt.plot(wl_sed,spectra)