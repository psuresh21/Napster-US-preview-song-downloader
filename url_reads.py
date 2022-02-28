import urllib.request

def url_reader(ask_music_url):
	# pass the ask_music_url in music_url
	music_url = ask_music_url
	read_the_url_page = urllib.request.urlopen(music_url)
	# BYTES SHOULD BE DECODE => UTF_8 FOR READABLE
	read_the_html = read_the_url_page.read().decode('utf_?')
	# SPLIT THE LEFT BRACKET
	html_as_list = read_the_html.split('<')
	return html_as_list
