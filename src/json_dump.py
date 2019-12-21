import os
import json

def main():
	dr = os.getcwd().replace('\\' ,'//')+'//source//'
	contents = os.listdir(dr)
	with open('json_dump_src.json' ,'w') as jsn:
		json.dump(contents ,jsn)

if __name__ == '__main__':
	main()