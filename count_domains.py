import json
"""
Author: 0kk
Statistics of count of domains in file

"""


def read_line_domain(file, separated):
	with open(file, 'r') as file:
		for line in file:
			if line.strip() == "":
				pass
			else:
				yield line.strip().split(separated)[1]

def statistics(file, output):
	result = {}
	for domain in read_line_domain(file, '@'):
		if domain not in result:
			result[domain] = 1
		else:
			result[domain] += 1
	with open(output, 'a') as output_w:
		dump_result = json.dumps(result)
		output_w.write(dump_result)
		print('[+] Done')
		print('[+] Result: ' + dump_result)
		print('[+] Saved at: ' + output)


if __name__ == '__main__':
	statistics('sbase.txt', 'statistics_base.txt')


