import pygmaps 
########## CONSTRUCTOR: pygmaps.maps(latitude, longitude, zoom) ##############################
# DESC:         initialize a map  with latitude and longitude of center point  
#               and map zoom level "15"
# PARAMETER1:   latitude (float) latittude of map center point
# PARAMETER2:   longitude (float) latittude of map center point
# PARAMETER3:   zoom (int)  map zoom level 0~20
# RETURN:       the instant of pygmaps
#========================================================================================
mymap = pygmaps.maps(8.491, 76.942, 15)


########## FUNCTION: setgrids(start-Lat, end-Lat, Lat-interval, start-Lng, end-Lng, Lng-interval) ######
# DESC:         set grids on map  
# PARAMETER1:   start-Lat (float), start (minimum) latittude of the grids
# PARAMETER2:   end-Lat (float), end (maximum) latittude of the grids
# PARAMETER3:   Lat-interval (float)  grid size in latitude 
# PARAMETER4:   start-Lng (float), start (minimum) longitude of the grids
# PARAMETER5:   end-Lng (float), end (maximum) longitude of the grids
# PARAMETER6:   Lng-interval (float)  grid size in longitude 
# RETURN:       no returns
#========================================================================================
#mymap.setgrids(37.42, 37.43, 0.001, -122.15, -122.14, 0.001)


########## FUNCTION:  addpoint(latitude, longitude, [color])#############################
# DESC:         add a point into a map and dispaly it, color is optional default is red
# PARAMETER1:   latitude (float) latitude of the point
# PARAMETER2:   longitude (float) longitude of the point
# PARAMETER3:   color (string) color of the point showed in map, using HTML color code
#               HTML COLOR CODE:  http://www.computerhope.com/htmcolor.htm
#               e.g. red "#FF0000", Blue "#0000FF", Green "#00FF00"
# RETURN:       no return
#========================================================================================
mymap.addpoint(8.491, 76.9421, "#0000FF")


########## FUNCTION:  addradpoint(latitude, longitude, radius, [color], title)##################
# DESC:         add a point with a radius (Meter) - Draw cycle
# PARAMETER1:   latitude (float) latitude of the point
# PARAMETER2:   longitude (float) longitude of the point
# PARAMETER3:   radius (float), radius  in meter 
# PARAMETER4:   color (string) color of the point showed in map, using HTML color code
#               HTML COLOR CODE:  http://www.computerhope.com/htmcolor.htm
#               e.g. red "#FF0000", Blue "#0000FF", Green "#00FF00"
# PARAMETER5:   title (string), label for the point
# RETURN:       no return 
#========================================================================================
mymap.addradpoint(8.491, (76.942), 95, '#FF0000')


########## FUNCTION:  addpath(path,[color])##############################################
# DESC:         add a path into map, the data struceture of Path is a list of points
# PARAMETER1:   path (list of coordinates) e.g. [(lat1,lng1),(lat2,lng2),...]
# PARAMETER2:   color (string) color of the point showed in map, using HTML color code
#               HTML COLOR CODE:  http://www.computerhope.com/htmcolor.htm
#               e.g. red "#FF0000", Blue "#0000FF", Green "#00FF00"
# RETURN:       no return
#========================================================================================
path = [(8.491, 76.942),(8.491, 76.941),(8.491, 76.94),(8.4911, 76.939)]
mymap.addpath(path,"#00FF00")

########## FUNCTION:  draw(file)######################################################
# DESC:         create the html map file (.html)
# PARAMETER1:   file (string) the map path and file
# RETURN:       no return, generate html file in specified directory
#========================================================================================
mymap.draw('./mymap.html')