
'''
reference 
* create a json dump to avoid ZEN
0) first run json file of .json to load
1) we check all files in source
2) list index = file number , value = file name
3) when we call this module it will create the file 
	and return the name of the file
4) for creating file [copy or rewrite(using open/close)] ? 
5) *** store a global counter for sanity and *uniqueity

'''

import os
import subprocess
import json
from shutil import copy
import json_dump

def main_echo(base ,dir_loc ,count):
	# base_src = os.getcwd().replace('\\' ,'//')+'//'
	copy_source = base + 'source//'

	# check if file is present or not
	dr_chk = base
	# os.path.exists(os.getcwd().replace('\\' ,'//')+'//'+'json_dump_src.json')
	if not os.path.exists(dr_chk+'json_dump_src.json//'):
		json_dump.main_call(copy_source)

	with open(base+'json_dump_src.json') as jsn:
		data = json.load(jsn)
	# print(len(data)) success
	# print(type(data))
	len_data = len(data)
	idx = count%len_data
	copy(copy_source+data[idx] , dir_loc)
	return data[idx]


def main():
	# main_echo(0)
	pass

if __name__ == '__main__':
	main()
	exit()