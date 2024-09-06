# from django.shortcuts import render
# from django.http import HttpResponse
# import zipfile
# from django.template import loader
# from django.contrib.auth.decorators import login_required
# from django.views import View
# import folium
# import geopandas as gpd
# from pykml import parser
# import io
# import shutil
# import numpy as np
# from os.path import splitext
# from .models import ssgi
# from django.core.files import File
# from django.core.files.storage import FileSystemStorage
# from django.db.models import Q
# import os
# import pyproj
# from django.conf import settings
# from datetime import datetime,date
# import xml.etree.ElementTree as ET
# from django.http import FileResponse,Http404
# from IPython.display import IFrame,HTML

# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
# from rest_framework.views import APIView
# from rest_framework import permissions
# from rest_framework.response import Response
# import json
# import requests
# import uuid

# from .serializers import SSGISerializer
# from .models import ssgi
# # Create your views here.

# class SSGIListView(ListAPIView):
#     queryset = ssgi.objects.all()
#     serializer_class = SSGISerializer
#     pagination_class = None

# class SSGIRetrieveView(RetrieveAPIView):
#     queryset = ssgi.objects.all()
#     serializer_class = SSGISerializer

# class SSGICreateView(CreateAPIView):
#     permission_classes = (permissions.IsAdminUser, )
#     queryset = ssgi.objects.all()
#     serializer_class = SSGISerializer

# class SSGISearchView(APIView):
#     def post(self, request, format=None):
#         data = self.request.data

#         foldercursor = ssgi.objects.filter().values()
#         intial_Acqu_time=datetime.now()
#         final_Acqu_time=datetime.now()
#         image_info=[]

#         try: 
#             cloud_coverage=data['cloudCoverage']
#             latitude=data['Latitude']
#             longitude=data['Longitude']
#             initial_date= data["initialdate_value"]
#             final_date=data["finaldate_value"]
#             satelliteId=data["Satellite_Type"]
#             product_level=data["Product_level"]
#             image_type=data["Image_Type"]
#         except:
#             return Response({'error': 'Please fill all required fields.'})

#         result=[]
#         for folder_row in foldercursor:
#             folder=folder_row.get('folder')
#             folderdirctories=os.listdir(folder)
#             for file in folderdirctories:
#                 path = folder
#                 if file.endswith('Report.xml'):
#                     result=xml_parser(path +"\\"+file,satelliteId,latitude,longitude,intial_Acqu_time,final_Acqu_time,product_level,cloud_coverage,image_type)
#                     print(result)
#                     if result[1]:                        
#                         for file in folderdirctories:
#                             if file.endswith('THUMB.jpg'):
#                                 thumbnail=(path +"\\"+file )
#                                 result[6]=folder
#                                 result[7]=thumbnail
#                         image_info.append(result)
     
#         return Response({'result', json.dumps(image_info)})


# @login_required(login_url='/authenticate/login')

# #TODO HOME PAGE
# def index(request):
#         if request.method == 'GET':
#             m = folium.Map(location=[9.005401,38.763611], zoom_start=9)
#             coordinates = (9.005401,38.763611)
#             folium.Marker(coordinates).add_to(m)

#             context = {"map": m._repr_html_()}
#             return render(request, 'sidebarquery/sidebar.html', context)




# def get(request):
 
#         iframe = serve_map()
#         intial_Acqu_time=datetime.now()
#         final_Acqu_time=datetime.now()
#         image_info=[]
#         coordinates_value=[]
#         invalid_file_flag='False'
#         flag='False'
#         if request.method == "POST":
#              flag='True'
#              cloud_coverage=request.POST['cloudCoverage']
#              latitude=request.POST['Latitude']
#              longitude=request.POST['Longitude']
#              initial_date= request.POST["initialdate_value"]
#              final_date=request.POST["finaldate_value"]
#              satelliteId=request.POST["Satellite_Type"]
#              product_level=request.POST["Product_level"]
#              image_type=request.POST["Image_Type"]
#              intial_Acqu_time=date_processor(initial_date)
#              final_Acqu_time=date_processor(final_date)
        
#              res = requests.get('http://localhost:8001/mainapp/test/')
#              cleaned_data = res.json() 
              
#              result=[]
#              for data in cleaned_data:
#                 id=data['id']
#                 folder=data['folder']
#                 for file in data['files']:
#                     path = 'http://localhost:8001'
#                     if file.endswith('Report.xml'):
#                         file_path = path + file
#                         x = ''
#                         data_read = requests.get(file_path).text
#                         for line in data_read.splitlines():
#                             x += line
#                         result=xml_parser(x,satelliteId,latitude,longitude,intial_Acqu_time,final_Acqu_time,product_level,cloud_coverage,image_type)
#                         if result[1]:                        
#                             for file in data['files']:
#                                 if file.endswith('THUMB.jpg'):
#                                     thumbnail=(path+file )
#                                     result[0] = id
#                                     result[6]=folder
#                                     result[7]=thumbnail
#                             image_info.append(result)


#         context = {
#             'coordinates': coordinates_value,
#              'map': iframe,
#              'result_value': image_info,
#              'flag':flag,
#              'file_flag':invalid_file_flag,
#              }
#         return render(request, 'sidebarquery/searchform.html',context)




# # TODO REMOVE THE FOLLOWING CLASS AS IT WAS IN FOR TESTING PURPOSE

# class ChooseFromMap(View):
#     def get(self, request):
#         log_message = "GET request received for fill_form"
#         print(log_message)
#         return HttpResponse(log_message)

#     def post(self, request):
#         log_message = "POST request received for fill_form"
#         print(log_message)
#         return HttpResponse(log_message)

# def display_html(request):
#        return render(request, 'sidebarquery/about.html')
# def feedback_view(request):
#        return render(request, 'feedback.html/')
# def home(request):
#        return render(request, 'index.html')




# def serve_lat_long(request):
#         flag='False'
#         coordinates_val=[]
#         coordinates_value=[]
#         iframe=serve_map()
        

#         if request.method == "POST":           
#             input_file_type=request.POST["KMLorShapefile"]
#             input_file=request.FILES["fileInput"]
           
           
#             if input_file_type=='kml_or_kmz':
#                 if splitext(input_file.name)[1]=='.kml':
#                       with open(os.path.join(settings.MEDIA_ROOT,'my_kml_file.kml'), 'wb+') as destination:
#                           for chunk in input_file.chunks():
#                               destination.write(chunk)
#                       coordinates_value=get_lat_long_kml()
#                 elif splitext(input_file.name)[1]=='.kmz':
#                     with open(os.path.join(settings.MEDIA_ROOT,'my_kmZ_file.kmz'), 'wb+') as destination:
#                        for chunk in input_file.chunks():
#                             destination.write(chunk)
#                     coordinates_value=get_lat_long_kmz()
#                 else:
#                      invalid_file_flag='False'

#             else:
#                 if splitext(input_file.name)[1]=='.zip':
                  
                  
#                     with open(os.path.join(settings.MEDIA_ROOT,'shape_file.zip'), 'wb+') as destination:
#                         for chunk in input_file.chunks():
#                             destination.write(chunk) 
#                     if is_zip_shapefile():
#                        coordinates_val=get_lat_long_Shape_file()   
#                     else:
#                        invalid_file_flag='False'




#         if coordinates_value:
#             print(coordinates_value)
#             invalid_file_flag='True'
#         else:
#             invalid_file_flag='False'
        



#         context = {
#                  'coordinates': coordinates_value,
#                  'map': iframe,
#                  'flag':flag,
#                  'file_flag':invalid_file_flag,
#                 }
#         return render(request, 'sidebarquery/searchform.html',context)




# def get_lat_long_kml():
#     coordinates =[]
#     with open(os.path.join(settings.MEDIA_ROOT,'my_kml_file.kml'), 'rb') as f:
#         root = parser.parse(f).getroot()
#         for i in root.findall('.//{http://www.opengis.net/kml/2.2}Point/{http://www.opengis.net/kml/2.2}coordinates'):
#            altitude_val=(i.text).find(',', (i.text).find(',') + 1)
#            coordinates.append(i.text[:altitude_val])
#         print(coordinates)
#         return coordinates
       



# def get_lat_long_kmz():
#     coordinates =[]
#     with zipfile.ZipFile(os.path.join(settings.MEDIA_ROOT,'my_kmZ_file.kmz'), 'r') as kmz:
#        kml_format = kmz.read('doc.kml')
#        root = ET.fromstring(kml_format)
#        for i in root.findall('.//{http://www.opengis.net/kml/2.2}Point/{http://www.opengis.net/kml/2.2}coordinates'):
#            altitude_val=(i.text).find(',', (i.text).find(',') + 1)
#            coordinates.append(i.text[:altitude_val])
#        print(coordinates)    
#        return coordinates



# def get_lat_long_from_zip_shape_file():
#     point_list=[]
#     sf = shapefile.Reader(os.path.join(settings.MEDIA_ROOT,'shape_file.zip'))
#     shapes = sf.shapes()
#     for shape in shapes:
#         for point in shape.points:
#             point_list.append(convert_cartesian_to_lat_long(point[0], point[1]))
#     print(point_list)





# def convert_cartesian_to_lat_long(x, y):
#     my_list=[]
#     p = pyproj.Proj("+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs")
#     lon, lat = p(x, y, inverse=True)
#     my_list.append(lat)
#     my_list.append(lon)
#     return my_list




# def get_lat_long_Shape_file():
#     dataframe = gpd.read_file(os.path.join(settings.MEDIA_ROOT,'shape_file.zip'))
#     coordinate_points = []
#     for geometry in dataframe['geometry']:
#         if geometry.geom_type == 'Polygon':
#             coordinates = list(geometry.exterior.coords)
#             coordinates = [convert_cartesian_to_lat_long(x, y) for x, y in coordinates]
#             # coordinate_points.append(coordinates)
#         elif geometry.geom_type == 'MultiPolygon':
#             for polygon in geometry:
#                 coordinates = list(polygon.exterior.coords)
#                 coordinates = [convert_cartesian_to_lat_long(x, y) for x, y in coordinates]
#               # coordinate_points.append(coordinates)
#     print(coordinates)
#     return coordinates








# def is_zip_shapefile():
#     counter=0
#     with zipfile.ZipFile(os.path.join(settings.MEDIA_ROOT,'shape_file.zip')) as zf:
#         for x in zf.namelist():
#               if x.endswith('.shp') or x.endswith('.shx') or  x.endswith('.prj') or x.endswith('.dbf'):
#                   counter = counter+1
                   
#         if counter == 4: 
                
#             return True
#         else:
#             return False  
  


# def serve_map():
#         map = folium.Map(location=[0, 0], zoom_start=4)

#         # Add a click event handler to the map
#         def handle_map_click(event):
#             lat, lon = event.latlng
#             marker = folium.Marker([lat, lon])
#             print(marker)
#             marker.add_to(map)

#         map.add_child(folium.ClickForMarker(popup="Click to add a marker"))
#         map.add_child(folium.LatLngPopup())
#         map.add_child(folium.LayerControl())
#         # Save the map as an HTML file
#         # map.save("map.html")

#         # Render the HTML file using the IFrame class
#         html = HTML(filename='map.html')
#         iframe = html.data.replace('\n', '').replace('\r', '')

#         return iframe



# def serve_image(request):
#     path = request.GET.get('image', '')
#     print("PATH", path)
#     image_data = requests.get(path)
#     return HttpResponse(image_data, content_type="image/jpeg")

# def generate_random_folder_name():
#     # Generate a random UUID
#     random_uuid = uuid.uuid4()
#     # Convert the UUID to a string and remove the hyphens
#     folder_name = str(random_uuid).replace('-', '')
#     return folder_name

# def download_zip(request):

#     dir_path = request.GET.get('dir_path', '')
#     res = requests.get('http://localhost:8001/mainapp/test/')
#     cleaned_data = res.json()
    
#     from urllib.parse import unquote
#     for ssgi_elem in cleaned_data:
#         if ssgi_elem['folder'] == unquote(dir_path.replace('% 5C', '\\')):
#             files = ssgi_elem['files']
#             break 
#     zip_filename = 'my_zip_file'

#     # Create a new zip file from the directory
#     new_folder_name = generate_random_folder_name()
#     destination_folder = settings.MEDIA_ROOT + '\\' + new_folder_name

#     if not os.path.exists(destination_folder):
#         os.makedirs(destination_folder)
    
#     for file_name in files:
#         file_data = requests.get('http://localhost:8001' + file_name)
#         print(file_name)
#         with open(destination_folder + '\\' + file_name[105:], 'wb') as file:
#             file.write(file_data.content)

#     shutil.make_archive(settings.MEDIA_ROOT + '\\' + new_folder_name, 'zip')

#     # Define the full path to the zip file
#     zip_path = os.path.join(settings.MEDIA_ROOT + '\\' + new_folder_name, zip_filename)
#     print(zip_path)
#     # Open the zip file in binary mode
#     with open(zip_path, 'rb') as f:
#         # Create a new HttpResponse object with the contents of the zip file
#         response = HttpResponse(f.read(), content_type='application/zip')
#         # Set the Content-Disposition header so that browsers present a download dialog
#         response['Content-Disposition'] ='inline; filename=' + os.path.basename(zip_path)
#         return response






# def xml_parser(xml_file,satellitename,latitude,longitude,intial_Acqu_time,final_Acqu_time,product_level,cloud_coverage,image_type,):
#     filetree = ET.ElementTree(ET.fromstring(xml_file))
#     root = filetree.getroot()
#     return_value=False
#     for data in root:
#       intial_Acquisition=datetime.strptime((data.find("imagingStartTime").text),'%Y %m %d %H:%M:%S.%f')
#       final_Acquisition=datetime.strptime((data.find("imagingStopTime").text),'%Y %m %d %H:%M:%S.%f')
#       sceneCenterLat =float(data.find("sceneCenterLat").text)
#       sceneCenterLong =float(data.find("sceneCenterLon").text)
#       productId =data.find("SourceProductID").text
#       cloudCoverage=int(data.find('cloudCoverage').text)
#       satelliteId =data.find("satelliteID").text
#       product_Type=data.find('productType').text
#       productLevel =data.find("productLevel").text
#       dataUpperLeftLat=data.find('dataUpperLeftLat').text
#       dataUpperLeftLon=data.find('dataUpperLeftLon').text
#       dataUpperRightLat=data.find('dataUpperRightLat').text
#       dataUpperRightLon=data.find('dataUpperRightLon').text
#       dataLowerLeftLat=data.find('dataLowerLeftLat').text
#       dataLowerLeftLon=data.find('dataLowerLeftLon').text
#       dataLowerRightLat=data.find('dataLowerRightLat').text
#       dataLowerRightLon=data.find('dataLowerRightLon').text
#       point1=dataUpperLeftLat+','+dataUpperLeftLon
#       point2=dataUpperRightLat+','+dataUpperRightLon
#       point3=dataLowerRightLat+','+dataLowerRightLon  
#       point4=dataLowerLeftLat+','+dataLowerLeftLon
    
#       if satelliteId==satellitename:
#           if productLevel==product_level:
#                if ((float(latitude))+20) >= sceneCenterLat and ((float(latitude))-20) <= sceneCenterLat :
#                    if ((float(longitude))+20) >= sceneCenterLong and ((float(longitude))-20) <= sceneCenterLong:
#                         if image_type==product_Type:
#                              if cloudCoverage<=(int(cloud_coverage)):
#                                  if intial_Acqu_time <= intial_Acquisition and final_Acqu_time >= final_Acquisition:
#                                        return_value=True
                                      

                                      
#     return_dict = {1: return_value,  2: satelliteId, 3:product_level,4:productId,5:cloudCoverage,8:point1,9:point2,10:point3,11:point4}
#     return return_dict



    

# def datechanger(date):
#     date=datetime.strptime(date,'%Y-%m-%d')
#     date=int(date.strftime('%Y%m%d'))*1000000
#     return date

# def date_processor(date):
#     date_obj= datetime.strptime(date, '%Y-%m-%d')
#     time = date_obj.replace(hour=0, minute=0, second=0, microsecond=0) 
#     return time


# def footprint_view(request, id):
#     res = requests.get('http://localhost:8001/mainapp/test/')
#     cleaned_data = res.json()

#     for ssgi_elem in cleaned_data:
#         if ssgi_elem['id'] == id:
#             files = ssgi_elem['files']
#             break

#     for file in files:
#         path = 'http://localhost:8001'
#         if file.endswith('Report.xml'):
#             file_path = path + file
#             x = ''
#             data_read = requests.get(file_path).text
#             for line in data_read.splitlines():
#                 x += line
#             filetree = ET.ElementTree(ET.fromstring(x))
#             root = filetree.getroot()
#             for data in root:
#                 intial_Acquisition=datetime.strptime((data.find("imagingStartTime").text),'%Y %m %d %H:%M:%S.%f')
#                 final_Acquisition=datetime.strptime((data.find("imagingStopTime").text),'%Y %m %d %H:%M:%S.%f')
#                 sceneCenterLat =float(data.find("sceneCenterLat").text)
#                 sceneCenterLong =float(data.find("sceneCenterLon").text)
#                 productId =data.find("SourceProductID").text
#                 cloudCoverage=int(data.find('cloudCoverage').text)
#                 satelliteId =data.find("satelliteID").text
#                 product_Type=data.find('productType').text
#                 productLevel =data.find("productLevel").text
#         if file.endswith('THUMB.jpg'):
#             thumbnail=(path +file )
#     context = {
#         'thumbnail': thumbnail,
#         'intial_Acquisition': intial_Acquisition,
#         'final_Acquisition': final_Acquisition,
#         'sceneCenterLat': sceneCenterLat,
#         'sceneCenterLong': sceneCenterLong,
#         'productId': productId,
#         'cloudCoverage': cloudCoverage,
#         'satelliteId': satelliteId,
#         'product_Type': product_Type,
#         'productLevel': productLevel,
#     }
#     return render(request, 'sidebarquery/footprint.html', context)


from django.shortcuts import render
from django.http import HttpResponse
import zipfile
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views import View
import folium
import geopandas as gpd
from pykml import parser
import io
import shutil
import numpy as np
from os.path import splitext
from .models import ssgi
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import os
import pyproj
from django.conf import settings
from datetime import datetime,date
import xml.etree.ElementTree as ET
from django.http import FileResponse,Http404
from IPython.display import IFrame,HTML
# Create your views here.

@login_required(login_url='/authenticate/login')

#TODO HOME PAGE
def index(request):
        if request.method == 'GET':
            m = folium.Map(location=[9.005401,38.763611], zoom_start=9)
            coordinates = (9.005401,38.763611)
            folium.Marker(coordinates).add_to(m)

            context = {"map": m._repr_html_()}
            return render(request, 'sidebarquery/sidebar.html', context)




def get(request):
 
        iframe = serve_map()
        foldercursor = ssgi.objects.filter().values()
        intial_Acqu_time=datetime.now()
        final_Acqu_time=datetime.now()
        image_info=[]
        coordinates_value=[]
        invalid_file_flag='False'
        flag='False'
        if request.method == "POST":
             flag='True'
             cloud_coverage=request.POST['cloudCoverage']
             latitude=request.POST['Latitude']
             longitude=request.POST['Longitude']
             initial_date= request.POST["initialdate_value"]
             final_date=request.POST["finaldate_value"]
             satelliteId=request.POST["Satellite_Type"]
             product_level=request.POST["Product_level"]
             image_type=request.POST["Image_Type"]
             intial_Acqu_time=date_processor(initial_date)
             final_Acqu_time=date_processor(final_date)
        
       
              
             result=[]
             for folder_row in foldercursor:
                folder=folder_row.get('folder')
                folderdirctories=os.listdir(folder)
                for levels in folderdirctories:
                    path=folder+'\\' +levels
                    dirctories=os.listdir(folder+'\\' +levels)
                    for file in dirctories:
                       if file.endswith('Report.xml'):
                           result=xml_parser(path +"\\"+file,satelliteId,latitude,longitude,intial_Acqu_time,final_Acqu_time,product_level,cloud_coverage,image_type)
                           if result[1]:                        
                              for file in dirctories:
                                if file.endswith('THUMB.jpg'):
                                    thumbnail=(path +"\\"+file )
                                    result[6]=folder
                                    result[7]=thumbnail
                              image_info.append(result)


        
        context = {
            'coordinates': coordinates_value,
             'map': iframe,
             'result_value': image_info,
             'flag':flag,
             'file_flag':invalid_file_flag,
             }
        return render(request, 'sidebarquery/searchform.html',context)




# TODO REMOVE THE FOLLOWING CLASS AS IT WAS IN FOR TESTING PURPOSE

class ChooseFromMap(View):
    def get(self, request):
        log_message = "GET request received for fill_form"
        print(log_message)
        return HttpResponse(log_message)

    def post(self, request):
        log_message = "POST request received for fill_form"
        print(log_message)
        return HttpResponse(log_message)

def display_html(request):
       return render(request, 'sidebarquery/about.html')
def feedback_view(request):
       return render(request, 'feedback.html/')
def home(request):
       return render(request, 'index.html')




def serve_lat_long(request):
        flag='False'
        coordinates_val=[]
        coordinates_value=[]
        iframe=serve_map()
        

        if request.method == "POST":           
            input_file_type=request.POST["KMLorShapefile"]
            input_file=request.FILES["fileInput"]
           
           
            if input_file_type=='kml_or_kmz':
                if splitext(input_file.name)[1]=='.kml':
                      with open(os.path.join(settings.MEDIA_ROOT,'my_kml_file.kml'), 'wb+') as destination:
                          for chunk in input_file.chunks():
                              destination.write(chunk)
                      coordinates_value=get_lat_long_kml()
                elif splitext(input_file.name)[1]=='.kmz':
                    with open(os.path.join(settings.MEDIA_ROOT,'my_kmZ_file.kmz'), 'wb+') as destination:
                       for chunk in input_file.chunks():
                            destination.write(chunk)
                    coordinates_value=get_lat_long_kmz()
                else:
                     invalid_file_flag='False'

            else:
                if splitext(input_file.name)[1]=='.zip':
                  
                  
                    with open(os.path.join(settings.MEDIA_ROOT,'shape_file.zip'), 'wb+') as destination:
                        for chunk in input_file.chunks():
                            destination.write(chunk) 
                    if is_zip_shapefile():
                       coordinates_val=get_lat_long_Shape_file()   
                    else:
                       invalid_file_flag='False'




        if coordinates_value:
            print(coordinates_value)
            invalid_file_flag='True'
        else:
            invalid_file_flag='False'
        



        context = {
                 'coordinates': coordinates_value,
                 'map': iframe,
                 'flag':flag,
                 'file_flag':invalid_file_flag,
                }
        return render(request, 'sidebarquery/searchform.html',context)




def get_lat_long_kml():
    coordinates =[]
    with open(os.path.join(settings.MEDIA_ROOT,'my_kml_file.kml'), 'rb') as f:
        root = parser.parse(f).getroot()
        for i in root.findall('.//{http://www.opengis.net/kml/2.2}Point/{http://www.opengis.net/kml/2.2}coordinates'):
           altitude_val=(i.text).find(',', (i.text).find(',') + 1)
           coordinates.append(i.text[:altitude_val])
        print(coordinates)
        return coordinates
       



def get_lat_long_kmz():
    coordinates =[]
    with zipfile.ZipFile(os.path.join(settings.MEDIA_ROOT,'my_kmZ_file.kmz'), 'r') as kmz:
       kml_format = kmz.read('doc.kml')
       root = ET.fromstring(kml_format)
       for i in root.findall('.//{http://www.opengis.net/kml/2.2}Point/{http://www.opengis.net/kml/2.2}coordinates'):
           altitude_val=(i.text).find(',', (i.text).find(',') + 1)
           coordinates.append(i.text[:altitude_val])
       print(coordinates)    
       return coordinates



def get_lat_long_from_zip_shape_file():
    point_list=[]
    sf = shapefile.Reader(os.path.join(settings.MEDIA_ROOT,'shape_file.zip'))
    shapes = sf.shapes()
    for shape in shapes:
        for point in shape.points:
            point_list.append(convert_cartesian_to_lat_long(point[0], point[1]))
    print(point_list)





def convert_cartesian_to_lat_long(x, y):
    my_list=[]
    p = pyproj.Proj("+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs")
    lon, lat = p(x, y, inverse=True)
    my_list.append(lat)
    my_list.append(lon)
    return my_list




def get_lat_long_Shape_file():
    dataframe = gpd.read_file(os.path.join(settings.MEDIA_ROOT,'shape_file.zip'))
    coordinate_points = []
    for geometry in dataframe['geometry']:
        if geometry.geom_type == 'Polygon':
            coordinates = list(geometry.exterior.coords)
            coordinates = [convert_cartesian_to_lat_long(x, y) for x, y in coordinates]
            # coordinate_points.append(coordinates)
        elif geometry.geom_type == 'MultiPolygon':
            for polygon in geometry:
                coordinates = list(polygon.exterior.coords)
                coordinates = [convert_cartesian_to_lat_long(x, y) for x, y in coordinates]
              # coordinate_points.append(coordinates)
    print(coordinates)
    return coordinates








def is_zip_shapefile():
    counter=0
    with zipfile.ZipFile(os.path.join(settings.MEDIA_ROOT,'shape_file.zip')) as zf:
        for x in zf.namelist():
              if x.endswith('.shp') or x.endswith('.shx') or  x.endswith('.prj') or x.endswith('.dbf'):
                  counter = counter+1
                   
        if counter == 4: 
                
            return True
        else:
            return False  
  


def serve_map():
        map = folium.Map(location=[0, 0], zoom_start=4)

        # Add a click event handler to the map
        def handle_map_click(event):
            lat, lon = event.latlng
            marker = folium.Marker([lat, lon])
            print(marker)
            marker.add_to(map)

        map.add_child(folium.ClickForMarker(popup="Click to add a marker"))
        map.add_child(folium.LatLngPopup())
        map.add_child(folium.LayerControl())
        # Save the map as an HTML file
        # map.save("map.html")

        # Render the HTML file using the IFrame class
        html = HTML(filename='map.html')
        iframe = html.data.replace('\n', '').replace('\r', '')

        return iframe



def serve_image(request, path):
    image_data = open( path, "rb").read()
    return HttpResponse(image_data, content_type="image/png")

    

def download_zip(request, dir_path):
    
    zip_filename = 'my_zip_file'

    # Create a new zip file from the directory
    shutil.make_archive(zip_filename, 'zip', dir_path)

    # Define the full path to the zip file
    zip_path = os.path.join(settings.MEDIA_ROOT, zip_filename)

    # Open the zip file in binary mode
    with open(os.path.join(settings.MEDIA_ROOT,'my_zip_file.zip'), 'rb') as f:
        # Create a new HttpResponse object with the contents of the zip file
        response = HttpResponse(f.read(), content_type='application/zip')
        # Set the Content-Disposition header so that browsers present a download dialog
        response['Content-Disposition'] ='inline; filename=' + os.path.basename(os.path.join(settings.MEDIA_ROOT, 'my_zip_file.zip'))
        return response






def xml_parser(xml_file,satellitename,latitude,longitude,intial_Acqu_time,final_Acqu_time,product_level,cloud_coverage,image_type,):
    filetree = ET.parse(xml_file)
    root = filetree.getroot()
    return_value=False
    for data in root:
      intial_Acquisition=datetime.strptime((data.find("imagingStartTime").text),'%Y %m %d %H:%M:%S.%f')
      final_Acquisition=datetime.strptime((data.find("imagingStopTime").text),'%Y %m %d %H:%M:%S.%f')
      sceneCenterLat =float(data.find("sceneCenterLat").text)
      sceneCenterLong =float(data.find("sceneCenterLon").text)
      productId =data.find("SourceProductID").text
      cloudCoverage=int(data.find('cloudCoverage').text)
      satelliteId =data.find("satelliteID").text
      product_Type=data.find('productType').text
      productLevel =data.find("productLevel").text
      dataUpperLeftLat=data.find('dataUpperLeftLat').text
      dataUpperLeftLon=data.find('dataUpperLeftLon').text
      dataUpperRightLat=data.find('dataUpperRightLat').text
      dataUpperRightLon=data.find('dataUpperRightLon').text
      dataLowerLeftLat=data.find('dataLowerLeftLat').text
      dataLowerLeftLon=data.find('dataLowerLeftLon').text
      dataLowerRightLat=data.find('dataLowerRightLat').text
      dataLowerRightLon=data.find('dataLowerRightLon').text
      point1=dataUpperLeftLat+','+dataUpperLeftLon
      point2=dataUpperRightLat+','+dataUpperRightLon
      point3=dataLowerRightLat+','+dataLowerRightLon  
      point4=dataLowerLeftLat+','+dataLowerLeftLon
    
      if satelliteId==satellitename:
          if productLevel==product_level:
               if ((float(latitude))+20) >= sceneCenterLat and ((float(latitude))-20) <= sceneCenterLat :
                   if ((float(longitude))+20) >= sceneCenterLong and ((float(longitude))-20) <= sceneCenterLong:
                        if image_type==product_Type:
                             if cloudCoverage<=(int(cloud_coverage)):
                                 if intial_Acqu_time <= intial_Acquisition and final_Acqu_time >= final_Acquisition:
                                       return_value=True
                                      

                                      
    return_dict = {1: return_value,  2: satelliteId, 3:product_level,4:productId,5:cloudCoverage,8:point1,9:point2,10:point3,11:point4}
    return return_dict



    

def datechanger(date):
    date=datetime.strptime(date,'%Y-%m-%d')
    date=int(date.strftime('%Y%m%d'))*1000000
    return date

def date_processor(date):
    date_obj= datetime.strptime(date, '%Y-%m-%d')
    time = date_obj.replace(hour=0, minute=0, second=0, microsecond=0) 
    return time







