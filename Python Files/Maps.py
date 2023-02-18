# Python program to get a google map 
# image of specified location using 
# Google Static Maps API
  
# importing required modules
import requests
  
# Enter your api key here
api_key = "AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0"
  
# url variable store url
url = "https://maps.googleapis.com/maps/api/staticmap?"
  
# center defines the center of the map,
# equidistant from all edges of the map. 
center = " Estadio Municipal José Trindade Lobo - Santo Antonio de Jesus - Bahia - Brasil "
  
# zoom defines the zoom
# level of the map
zoom = 10
  
# get method of requests module
# return response object
r = requests.get(url + "&size=400x400&center="+center+
                        "&zoom="+str(zoom)+"&maptype=satellite&key="+api_key)
print(url + "&size=400x400&center="+center+
                        "&zoom="+str(zoom)+"&maptype=satellite&key="+api_key)
#https://maps.googleapis.com/maps/api/staticmap?&size=400x400&center=Tokyo&zoom=10&maptype=satellite&key=AIzaSyDcz_OKnoD8j0n-a_3AyipLXOb6ZyqFI-0
# wb mode is stand for write binary mode
f = open('F:/Users/SAMUEL/Desktop/Nova pasta (2)/ll.jpeg', 'wb')
  
# r.content gives content,
# in this case gives image
f.write(r.content)
  
# close method of file object
# save and close the file
f.close()