## Installation ##

Install lib with pip:

	pip install doccito

**- OR -**

Put the "doccito" `directory` somewhere in your python path


## Usage ##

Doccito allows quick and easy documentation for your project by taking a readme.markdown file and constructing an html page with a table of contents corresponding to the document's <\h\> tags.

More markdown syntax and examples can be found on the Markdown website, <a href = "http://daringfireball.net/projects/markdown/syntax">here</a>.

###Command-Line Arguments###

Running Doccito on the command-line allows use of either a provided base.html page for your document or a custom one with the [--template] command.

Running Doccito without any arguments will bring up it's help menu with optional arguments:

    -h, --help     show help message and exit
    --stdio        specifies stdio
    --template     specifies custom html template
    --version      show program's version number and exit


	cat README.markdown | python doccito.py --stdio > docs.html

**- OR -**

	python doccito.py README.markdown > docs.html

will take the README.markdown file and throw it into the default base.html template and create and send it to docs.html.

	cat README.markdown | python doccito.py --stdio --template layout.html > docs.html

will use layout.html as it's template.



##API##

Using Doccito as a library allows use of several functions:

###doccito.create_docs###

  - `input` is a string containing the documentation in .markdown
  - `template` is the .html template to be used (optional)

Example usage:

    import doccito

    doccito.create_docs(input, template="./base.html")