import flickrapi
import json 

api_key = 'fc9d33a60904a30be522a6f6f98365dc'
api_secret = '55f69ea50c2eb01f'

# Flickr API 
f = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# to convert date to Unix datetime use: http://www.epochconverter.com/
photos = f.photos_search(tags='new york', per_page=1, text='New York', min_upload_date=1427897394)

# to pretty print the json photos, uncomment following line:
# print json.dumps(photos, indent=4, separators=(',', ':'))

# owner of the photo
owner = photos['photos']['photo'][0]['owner']
# the ID of the photo
photo_id = photos['photos']['photo'][0]['id']

# example of a link to a photo
# https://www.flickr.com/photos/67832671@N00/5484008696/
# we create link to our own photo
url = 'https://www.flickr.com/photos/%s/%s/' % (owner, photo_id)

# display url
print url
