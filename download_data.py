
import requests

for l in range (361):
    url = 'https://www.astro.uni-bonn.de/hisurvey/euhou/LABprofile/downloadrot.php?ral='+str(l)+'&decb='+str(0)+'&csys=0&beam=0.60'
        #url = 'https://www.astro.uni-bonn.de/hisurvey/euhou/LABprofile/download.php?ral='+str(l)+'&decb='+str(b)+'&csys=0&beam=0.60'
    myfile = requests.get(url)
        #name = 'hi_b-'+str(b)+'_l-'+str(l)+'.txt'
    name = 'rotation_b-'+str(0)+'_l-'+str(l)+'.txt'
    open(name, 'wb').write(myfile.content)