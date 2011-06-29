from os.path import join, abspath, dirname
import sys
import re
import markdown
from optparse import OptionParser

here = lambda *args: join(abspath(dirname(__file__)), *args)

__VERSION__ = "0.1"
get_version = lambda: __VERSION__


def render_content(markup, format="markdown"):
	if format == 'markdown':
		return markdown.markdown(markup, output_format='html')


slug_finder = re.compile(r"[a-zA-Z0-9_-]+")
slugs = set()
def slugify(header_text):
	id = "-".join(slug_finder.findall(header_text))

	uniq_id = id
	i = 1
	while uniq_id in slugs:
		uniq_id = "%s-%s" % (id, i)
		i += 1

	slugs.add(uniq_id)
	return uniq_id


section = re.compile(r"<(h[23])>(.*?)</h\d>")
def build_toc(html):
	toc = []
	def callback(m):
		tag, title = m.groups()
		slug = slugify(title)

		toc.append('<a href="#%(slug)s" class="%(tag)s">%(title)s</a>' % locals())

		return '<%(tag)s id="%(slug)s">%(title)s</%(tag)s>' % locals()

	new_html = section.sub(callback, html)

	return '\n'.join(toc), new_html


def create_docs(input, template=here("./base.html")):
	html = render_content(input)
	toc, html = build_toc(html)

	template = open(template).read()

	output = template.replace("{{ content }}", html)
	output = output.replace("{{ toc }}", toc)

	return output

