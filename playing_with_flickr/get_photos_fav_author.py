from __future__ import print_function
import flickrapi

api_key = 'fc9d33a60904a30be522a6f6f98365dc'
api_secret = '55f69ea50c2eb01f'

# Flickr API 
f = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
# My favorite author
author = '67832671@N00'
# Put 3 photo IDs into below list
photo_ids = []
# Get 3 photos
photos = f.photos_search(per_page=3, user_id=author)
# Print links to 3 photos
for index, photo in enumerate(photos['photos']['photo']):
	photo_ids.append(photo['id'])
	print('https://www.flickr.com/photos/%s/%s/' % (author, photo_ids[index]))
