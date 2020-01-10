import os
import time
import json

def main_call(dr):
	if not os.path.exists(dr):
		print('\n\n\n\n')
		print('source folder not found ')
		print('extract the source.rar file ')
		print('press    "Ctrl + C" to exit')
		time.sleep(1000)

	contents = os.listdir(dr)
	with open('json_dump_src.json' ,'w') as jsn:
		json.dump(contents ,jsn)

def main():
	dr = os.getcwd().replace('\\' ,'//')+'//source//'
	main_call(dr)

if __name__ == '__main__':
	main()
	exit()