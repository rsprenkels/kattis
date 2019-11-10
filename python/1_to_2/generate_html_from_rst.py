import docutils.core
docutils.core.publish_file(
    source_path="docu.rst",
    destination_path="output.html",
    writer_name="html")

html = open("output.html").read()