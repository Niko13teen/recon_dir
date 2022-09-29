import argparse
import requests


def request(url):
	try:
		return requests.get("https://" + url)
	except requests.exceptions.ConnectionError:
		pass

def recon_dir(file_name, target_url):
	file = open(file_name, 'r')
	for line in file:
		directory = line.strip()
		full_url = target_url + '/' + directory
		response = request(full_url)
	if response:
		print('[+] Discovered Directory At This Path: ' + full_url)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--target', '-t',
						action='store',
						dest='target',
						help='Enter target')
	parser.add_argument('--file', '-f',
						action='store',
						dest='file',
						help='file input')
	args = parser.parse_args()
	target_url, file_name = args.target, args.file
	recon_dir(file_name, target_url)
