import MeshData


# site_main = 'footpatrol' or 'jdsports' or 'size'
# region = ISO Code e.g. GB or NL etc...

site_main = 'footpatrol'
region = 'GB'
header_data_api = MeshData.Taskslist.region_api_selec(site_main,region.lower())

#return json format for details needed for hawk auth header creation
print(header_data_api)