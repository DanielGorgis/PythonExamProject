import pygal
import pandas

#Importerer pandas for at specificere hvilke kolonner der skal gøres brug af
df = pandas.read_csv('datafile.csv',header=0,usecols=['district'], index_col=['district'])


pandas.set_option('display.max_columns', 50000)


print(df.head(7856))


df.to_csv("sample3.csv",index_label="district")

#opretter ny CSV fil med det data vi har scrapet


df2 = pandas.read_csv("sample3.csv")


#print(df2.head())


#søger efter hvor mange distrikter der af i csv filen af følgende 1,2,3,4,5,6 hvorfor for-loopet finder frem til resultatet

count1=0
count2=0
count3=0
count4=0
count5=0
count6=0

f=open('sample3.csv','r')
district_count = f.readlines()

#undgår redundant kode ved at bruge samme forloop

for line in district_count:
    if "6" in line:
        count6=count6+1
    if "5" in line:
        count5 = count5 + 1
    if "4" in line:
        count4=count4+1
    if "3" in line:
        count3=count3+1
    if "2" in line:
        count2=count2+1
    if "1" in line:
        count1=count1+1

print("dis 6",count6)
print("dis 5",count5)
print("dis 4",count4)
print("dis 3",count3)
print("dis 2",count2)
print("dis 1",count1)

f.close()

#opretter piechart ved brug af pygal modul til at vise statistik grafisk som .svg fil

piechart = pygal.Bar()
piechart.add('District 1',count1)
piechart.add('District 2',count2)
piechart.add('District 3',count3)
piechart.add('District 4',count4)
piechart.add('District 5',count5)
piechart.add('District 6',count6)

#således ses det nedenfor. fil er oprettet og kan åbnes
piechart.render_to_file('crimerates.svg')