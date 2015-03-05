
#from  gtexpmapfunc import gtexpmapfunc

import subprocess
import pyfits
import cfg




def gtselectfunc(healpix,ra,dec,week1,week2):
				
	if week1!=week2:
		identity="%06d_%d_%d_w%03d_w%03d" %(healpix,ra,dec,week1,week2)
		ltcube="%s/lat_ltcube_weekly_w%03d_w%03d_p203_v001.fits" %(cfg.home,week1,week2)
	else:
			identity="%06d_%d_%d_w%03d" %(healpix,ra,dec,week1)
			ltcube="%s/lat_spacecraft_weekly_w%03d_p203_v001_ltcube.fits" %(cfg.home,week1)
	radius=int(cfg.radius)
	region_filtered="%s_region_filtered_gti.fits" %(identity)
	events="%s_events.txt" %(identity)
		
	with open(events, 'w') as outputFile:
		for x in range(week1,week2+1):
			outputFile.write("%s/lat_photon_weekly_w%03d_p202_v001_gti.fits\n" % (cfg.home,x))
	
	header=pyfits.getheader("%s" %(ltcube)) 
	header.keys()

	time=header['TSTART']
	stop=header['TSTOP']
      
	with open("%s_output.log" % (identity),"a") as outputFile:
		proc=subprocess.Popen(['gtselect'],stdin=subprocess.PIPE,stdout=outputFile)
		proc.communicate('@%s\n\
%s\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n\
%f\n' %(events,region_filtered,ra,dec,radius,time,stop,cfg.lowerenergy,cfg.upperenergy,cfg.zenith))
'''
if __name__ == "__main__":
    import sys
    gtselectfunc(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
'''
