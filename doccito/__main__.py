import sys
from optparse import OptionParser
from doccito import get_version
from doccito.doc_generator import create_docs

def main():
	parser = OptionParser(description='Input a custom html template with --html', version='Doccito v' + get_version())
	parser.add_option('--stdio', action='store_true', help='specifies stdio', dest='stdio')
	parser.add_option('--template', help='specifies custom html template')
	
	options, args = parser.parse_args()
	
	if options.stdio:
		input = sys.stdin.read()
	
	elif len(args):
		input = open(args[0]).read()
	
	else:
		parser.parse_args(['--help'])
		sys.exit(0)
	
	kwargs = {}
	if options.template:
			kwargs['template'] = options.template
	
	output = create_docs(input, **kwargs)
	sys.stdout.write(output)

if __name__ == '__main__':
	main()

