import flickrapi

api_key = 'fc9d33a60904a30be522a6f6f98365dc'
api_secret = '55f69ea50c2eb01f'

# Flickr API 
f = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
# to convert date to Unix datetime use: http://www.epochconverter.com/
photos = f.photos_search(per_page=5, text='New York', min_upload_date=1427897394)
owners, photo_ids, urls = [], [], []
for index, photo in enumerate(photos['photos']['photo']):
	# owners of the photos
	owners.append(photo['owner'])
	# the IDs of the photos
	photo_ids.append(photo['id'])
	urls.append('https://www.flickr.com/photos/%s/%s/' % (owners[index], photo_ids[index]))

# display urls
for url in urls:
	print url
