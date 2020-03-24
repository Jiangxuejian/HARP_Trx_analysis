from os import path
from astropy.table import Table
import re
import numpy as np

f1=Table.read('sql_result.txt',format='ascii.tab')

f2= open("filelist.txt","w+")
f2=Table(data=np.zeros([14*len(f1),len(f1[0])]),dtype=f1.dtype)
f2['receptor']= ''
f2['trx'] = 0.
for i in range(0,len(f1)):
	date= str(f1[i][0])
	num = format(f1[i][1], '05d')
	filename = f1[i][4]
	#print(date,num,filename)
	newpath = path.join('/jcmtdata/raw/acsis/spectra/',date,num,filename)
	trx=popen('hdstrace '+ newpath +'.more.acsis.trx newline nlines=1 eachline width=400').read()
	trx_arr = re.findall("\d+\.\d+", trx)[0:14]
	#np.reshape(trx_arr[0:14], (len(trx_arr)//14, 14))[0]
	receptor=popen('hdstrace '+ newpath +'.more.acsis.receptors newline nlines=14 eachline').read()
	rec_arr = re.findall("H\d+\d+", receptor)
	#rec_arr = np.reshape(rec_arr, (1,len(rec_arr)))[0]
	for j in range(14):
		f2[f1.colnames][14*i + j] = f1[i]
		f2['receptor'][14*i+j] = rec_arr[j]
		f2['trx'][14*i+j] = trx_arr[j]
