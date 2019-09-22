import pandas as pd
#to append email id's to clinics

df=pd.read_csv('clinics.csv')
l=(~df["Email"].str.endswith('@myclinic.com.au'))
#for i in df[l]["Email"]:
a=list(df["Email"])
b=[]
string='@myclinic.com.au'
for x in a:
    if not x.endswith('@myclinic.com.au'):
      x=x + '@myclinic.com.au'
      b.append(x)
    else:
        x=x
        b.append(x)
df["Email"]=b
df.to_csv('clinics3.csv')
 
#To fetch Lat,Lon from Json file to csv file 

dfcols = ['ClinicID', 'Lat', 'Lon']
df_xml = pd.DataFrame(columns=dfcols)
import xml.etree.ElementTree as ET
tree=ET.parse('cliniclocations.xml')
root=tree.getroot()
#print(root)
for clinic in root.iter('clinic'):
    Lat=clinic.find('Lat').text
    Lon=clinic.find('Lon').text
    ID=clinic.find('ClinicID').text
    #print(ID,Lat,Lon)
    df_xml = df_xml.append(
    pd.Series([ID,Lat,Lon], index=dfcols),
    ignore_index=True)

df_xml.to_csv('locations.csv')


#Merge data from all files
clinics = pd.read_csv('clinics3.csv')
clinicsservices = pd.read_csv('clinicservices.csv')
services = pd.read_csv('services.csv')
cliniclocations = pd.read_csv('locations.csv')

final = pd.merge(clinics, clinicsservices, on='ClinicID', how='outer')
final = pd.merge(services, final, on='ServiceID', how='outer')
final = pd.merge(cliniclocations, final, on='ClinicID', how='outer')
final.to_csv('clinicservicelocations2.csv')
final_pd=pd.read_csv('clinicservicelocations2.csv', index_col = False)
#final_pd.drop(final_pd.columns[[0, 1]], axis=1, inplace=True)
final_pd["Email"].replace('\s+', '',regex=True,inplace=True)