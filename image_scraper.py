import requests
import urlparse
from lxml import html

call = 0
def get_image( urls ):
	global call
	call += 1
	for url in urls:
		req = requests.get(url)
		try:
			htmlCode = html.fromstring(req.text)
			imageTags = htmlCode.xpath('//img/@src')
			print imageTags
			# print inbounds
			inbounds = abs_filter(htmlCode.xpath('//a/@href'), url)
			imageDump = abs_filter(imageTags, url)
		except:
			print "cannot scrape this " + url
	print imageDump
	# print inbounds
	while call <= 1:
		get_image(inbounds)

def abs_filter(sTags, url):
	absTags = []
	for tag in sTags:
		if not bool(urlparse.urlparse(tag).netloc):
			absTags.append(url + tag)
		else:
			absTags.append(tag)
	return absTags

get_image(["http://www.dpgraph.com/"])

# get_image(inbounds)