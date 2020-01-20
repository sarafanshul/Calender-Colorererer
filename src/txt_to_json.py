import json

def main():
	# loading data
	data_set = set() 

	with open('commit_extra.txt' , 'r') as data:
		for line in data:
			line = line.strip()
			data_set.add(line)

	with open('commit-messages_small.json' ,'r') as jsn:
		data = json.load(jsn)
		# print(type(data)) # dict
		data = set(data["messages"])

	# merging data
	data_out_dump = data_set | data
	# print(len(data_out_dump)) # successfull merge

	# dumping data
	with open('commit-messages.json' ,'w') as jsn:
		json.dump(list(data_out_dump) ,jsn) # use dumps insted of dump


if __name__ == '__main__':
	main()