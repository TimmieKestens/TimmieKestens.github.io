#Parsing and extracting
data = "From Kathleen to timkestens@yahoo.co.uk Sun 30 april 2000"
whereat = data.find("@")
print (whereat)
wherespace = data.find(" ", whereat)
print (wherespace)
emailprovider = data[whereat+1 : wherespace]
print (emailprovider)# Write your code here :-)
