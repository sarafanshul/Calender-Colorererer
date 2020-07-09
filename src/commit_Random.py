import json
import os

def commit_Str(base ,count):
	with open(base+'commit-messages.json') as jsn:
		data = json.load(jsn)
		# print(data ,type(data))
	lent = len(data)
	# print(*data['messages'] ,sep = '\n')
	return data[count%lent]
	

def main():
	commit_Str('' ,3)

if __name__ == '__main__':
	main()