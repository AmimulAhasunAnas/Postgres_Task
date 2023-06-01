import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(database="usadeath",
                        host="localhost",
                        user="postgres",
                        password="Anas907",
                        port="5432")
data=pd.read_csv('usa_country_wise.csv')
rows=data.shape[0]
cur=conn.cursor()
#cur.execute('create table usa_death(id SERIAL PRIMARY KEY,province_state varchar(20),country_region varchar(10),lat float,lon float,date_ date,confirmed int,deaths  int);')
#for i in range(0,rows):
 #cur.execute('insert into usa_death values(%s,%s,%s,%s,%s,%s,%s,%s)',(i,data['Province_State'][i],data['Country_Region'][i],data['LAT'][i],data['LON'][i],data['Date'][i],int(data['Confirmed'][i]),int(data['Deaths'][i])))
#conn.commit()

cur.execute('select confirmed,deaths from usa_death')
allrows=cur.fetchall()
print(allrows)

cur.execute('select sum(deaths) as total_deaths,sum(confirmed) as Total_confirmed_deaths from usa_death')
allrows=cur.fetchall()
print(allrows)

# Plot the histogram
plt.hist(data['Confirmed'], bins='auto')
plt.xlabel('Confirmed Cases')
plt.ylabel('Frequency')
#plt.hist(data['Deaths'], bins='auto')
#plt.xlabel('Death Cases')
#plt.ylabel('Frequency')
plt.title('Histogram of Covid Confirmed Deaths')
plt.savefig("Histogram(ConfirmedDeath).png")
plt.show()