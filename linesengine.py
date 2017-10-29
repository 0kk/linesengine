#!/usr/bin/python3

from tqdm import tqdm
from beautifultable import BeautifulTable
from optparse import OptionParser
import os
"""

// Author: 0kk
// Statistics count of domains in file

"""

current_dir = os.path.abspath(__file__)
packing_dir = current_dir + '/packed'		



def read_line(file):
	with open(file, 'r') as file:
		gen_normalize = (ln.replace(';',':') for ln in file)
		for line in gen_normalize:
			if line.strip() == "":
				pass
			else:
				yield line


def statistics(file, output, packing=False):
	result = {}
	for line in tqdm(read_line(file), desc='Processing db of lines...', ascii=True):
		try:
			domain = line.strip().split('@')[1].split(':')[0]
		except:
			pass
		if domain not in result:
			result[domain] = 1
			if packing == True:
				os.mkdir('packed/' + str(domain))
				with open('packed/' +str(domain) + '/' + str(domain) + '.txt', 'a') as packing_file:
					packing_file.write(line + '\n')
		else:
			if packing == True:
				with open('packed/' +str(domain) + '/' + str(domain) + '.txt', 'a') as packing_file:
					packing_file.write(line + '\n')
			result[domain] += 1
			
	with open(output, 'w') as output_w:
		sorted_tuples_lst = sorted([(k,v) for (k,v) in tqdm(result.items(), ascii=True ,desc='Sorting tuples...')],
			key=lambda tup: tup[1], reverse=True)
		output_w.write('[DOMAINS] \n\n')
		table = BeautifulTable()
		table.column_headers = ['Domains', 'Count']
		for item in tqdm(sorted_tuples_lst, ascii=True ,desc='Creating of table...'):
			table.append_row([item[0], item[1]])
		output_w.write(str(table) + '\n')

		print('[+] Done')
		print('[+] Result table + \n' + str(table))
		print('[+] Saved at ' + output)


if __name__ == '__main__':
	parse=OptionParser("""
	 
	

	
 _      __________       _______  _______ _______ _       _________________       _______            __     _______ 
( \     \__   __( (    /(  ____ \(  ____ (  ____ ( (    /(  ____ \__   __( (    /(  ____ \  |\     //  \   (  __   )
| (        ) (  |  \  ( | (    \/| (    \/ (    \/  \  ( | (    \/  ) (  |  \  ( | (    \/  | )   ( \/) )  | (  )  |
| |        | |  |   \ | | (__    | (_____| (__   |   \ | | |        | |  |   \ | | (__      | |   | | | |  | | /   |
| |        | |  | (\ \) |  __)   (_____  )  __)  | (\ \) | | ____   | |  | (\ \) |  __)     ( (   ) ) | |  | (/ /) |
| |        | |  | | \   | (            ) | (     | | \   | | \_  )  | |  | | \   | (         \ \_/ /  | |  |   / | |
| (____/\__) (__| )  \  | (____/\/\____) | (____/\ )  \  | (___) |__) (__| )  \  | (____/\    \   / __) (__|  (__) |
(_______|_______//    )_|_______/\_______|_______//    )_|_______)_______//    )_|_______/     \_/  \____(_|_______)
                                                                                                                    
[by 0kk]
	 
	 
	./linesengine.py [options]
	 
	options:
	 
	-i,--url     [::] Input db file 
	-o,--output  [::] Output result file
	-p,--packing [::] Packing of lines
	 
	[+] usage:
	 
	./linesengine.py -i db.txt -o db_result.txt
	./linesengine.py -i db.txt -o db_result.txt -p true
	
	""")
	parse.add_option('-i','--input',dest='I',type='string',help='Input db file')          
	parse.add_option('-o','--output',dest='O',type='string',help='Output result file')
	parse.add_option('-p','--packing',dest='P',help='Packing of lines', action="store_true", default=False)
	 
	(opt,args) = parse.parse_args()
 
	if opt.I == None and opt.O == None:
		print(parse.usage)
		exit(0)
	elif opt.I != None and opt.O != None and opt.P == False:
		statistics(opt.I, opt.O)
	else:
		statistics(opt.I, opt.O, True)




