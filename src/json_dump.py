import os
import json

def main_call(dr):
	contents = os.listdir(dr)
	with open('json_dump_src.json' ,'w') as jsn:
		json.dump(contents ,jsn)

def main():
	dr = os.getcwd().replace('\\' ,'//')+'//source//'
	main_call(dr)

if __name__ == '__main__':
	main()
	exit()