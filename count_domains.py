#!/usr/bin/python3

from beautifultable import BeautifulTable
import json

"""

// Author: 0kk
// Statistics count of domains in file

"""

			



def read_line_domain(file, separated):
	with open(file, 'r') as file:
		gen_normalize = (ln.replace(';',':') for ln in file)
		for line in gen_normalize:
			if line.strip() == "":
				pass
			else:
				try:
					yield line.strip().split(separated)[1].split(':')[0]
				except:
					pass



def statistics(file, output):
	result = {}
	for domain in read_line_domain(file, '@'):
		if domain not in result:
			result[domain] = 1
		else:
			result[domain] += 1
	with open(output, 'w') as output_w:
		dump_result = json.dumps(result)
		sorted_tuples_lst = sorted([(k,v) for (k,v) in result.items()],
			key=lambda tup: tup[1], reverse=True)
		output_w.write('\n\n\n\n [DOMAINS] \n\n')
		table = BeautifulTable()
		table.column_headers = ["Domain", "Count"]
		for item in sorted_tuples_lst:
			table.append_row([item[0], item[1]])
		output_w.write(str(table) + '\n')

		print('[+] Done')
		print('[+] Result table + \n' + str(table))
		print('[+] Saved at ' + output)


if __name__ == '__main__':
	statistics('sbase.txt', 'statistics_base.txt')



