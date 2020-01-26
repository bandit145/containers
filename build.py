#!/usr/bin/env python3
import argparse
import docker
import os
import sys
import json
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='build containers')
parser.add_argument('-d', '--dir', help='directory to build from. If not used builds all')
parser.add_argument('-t', '--tag', help='tag for build')
parser.add_argument('-l', '--labels', help='labels in label=thing,label2=thing')
parser.add_argument('-p', '--push', help='push container when done')
parser.add_argument('--test', help='run tests before pushing')
parser.add_argument('-w', '--workers', help='number of workers', type=int, default=4)

args = parser.parse_args()


def get_labels(labels):
	label_dict = {}
	if labels:
		for item in labels.split(','):
			if '=' not in item:
				print('==> {0} syntax incorrect'.format(item), file=sys.stderr)
				sys.exit(1)
			key, value = item.split('=')
			label_dict[key] = item
		return label_dict
	else:
		return None


def build_container(client, cont, tag, labels={}):
	try:
		print('==> Starting build of container {0}'.format(cont))
		image = client.images.build(path=cont, tag=tag, labels=labels, rm=True, forcerm=True)
		[print('==>', x['stream']) for x in image[1]]
		return image
	except docker.errors.BuildError as error:
		print('==> Build failure', str(error), file=sys.stderr)
		sys.exit(1)
	except: docker.errors.APIError:
		print('==> Docker API error. Is the docker daemon running? or do you have permission?')
		sys.exit(1)


def test_container(cont):
	print('==> Starting test of container {0}'.format(cont))
	pass


def push_container(client, cont):
	print('==> Pushing container {0}'.format(cont))
	pass


def get_cont_info(cont):
	try:
		with open(cont + '/info.json', 'r') as cont_info:
			return json.load(cont_info)
	except IOError:
		print('==> Could not find {0}'.format(cont + '/info.json'), file=sys.stderr)
		sys.exit(1)
	except json.JSONDecodeError:
		print('==> Json decode error for {0}'.format(cont + '/info.json'), file=sys.stderr)
		sys.exit(1)


def container_process(client, labels):
	dirs = [x for x in os.listdir('.')]
	if args.dir and args.dir in dirs:
		build_container(client, args.dir, args.tag, labels)
		if args.test:
			test_container()
		if args.push:
			push_container()
	elif cont not in dires and args.dir:
		print('==> Container {0} not found'.format(cont), file=sys.stderr)
		sys.exit(1)
	
	# if not args.container:
	# 	print('==> No specific container specified building all')
	# 	pool = Pool(args.workers)
	# 	pool.map(build_container, client, cont, tag, labels)
	# 	if args.test:
	# 		pool.map(test_container)


def main():
	client = docker.from_env()
	labels = get_labels(args.labels)
	container_process(client, labels)

if __name__ == '__main__':
	main()