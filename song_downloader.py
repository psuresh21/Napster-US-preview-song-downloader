

def preview_download_napster(html_as_list):
	count_the_song = 0
	for m in html_as_list:
		if 'preview_url' in m:
			count_the_song = count_the_song + 1
			m = m.split(' ')
			track_names = ''.join(s for s in m if 'track_shortcut' in s)
			spt_url_sng = ''.join(s for s in m if 'preview_url' in s)
			print(
			str(count_the_song).center(5),
			'\tSONG NAME -\n\t%s \n\tDOWNLOADABLE LINK-\n\t%s\n' %
			(track_names.split('=')[1],
			spt_url_sng.split('=')[1]),
			'--------------------------------------------------------------')
