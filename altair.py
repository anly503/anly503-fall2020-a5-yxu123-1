import pandas as pd
import altair as alt
import numpy as np
household_data= pd.read_excel(r'C:\Users\13448\Desktop\new\datatest.xlsx')
#print(household_data)
#interval = alt.selection_interval()
chart1=alt.Chart(household_data).mark_line(color='#20FCBC').encode(
    x =alt.X('Date',title='Time[year/month/day]') ,
    y = alt.Y('TAP20',title='Lamp-Electricity-Comsumptation') ,

).properties(
    width=300,height=300,title='household06-Lamp'
).interactive()

chart2=alt.Chart(household_data).mark_line(color='#e30000').encode(
    x =alt.X('Date',title='Time[year/month/day]') ,
    y = alt.Y('TAP21',title='Laptop-Electricity-Comsumptation') ,

).properties(
    width=300,height=300,title='household06-Laptop'
).interactive()

chart3 = alt.Chart(household_data).mark_line(opacity=0.3,color='#626262').encode(
    x=alt.X('Date',title='Time[year/month/day]'),
    y=alt.Y('TAP22',title='Router-Electricity-Comsumptation') ,

).properties(
    width=300,height=300,title='household06-Router'
).interactive()

chart4 = alt.Chart(household_data).mark_line(opacity=0.3,color='#ffff15').encode(
    x=alt.X('Date',title='Time[year/month/day]'),
    y=alt.Y('TAP23',title='Coffee machine-Electricity-Comsumptation') ,

).properties(
    width=300,height=300,title='household06-Coffee machine'
).interactive()

chart5 = alt.Chart(household_data).mark_line(opacity=0.3,color='#929391').encode(
    x=alt.X('Date',title='Time[year/month/day]'),
    y=alt.Y('TAP24',title='Entertainment  -Electricity-Comsumptation') ,

).properties(
    width=300,height=300,title='household06-Entertainment '
).interactive()

chart6 = alt.Chart(household_data).mark_line(opacity=0.3,color='#0e8eff').encode(
    x=alt.X('Date',title='Time[year/month/day]'),
    y=alt.Y('TAP25',title='Fridge-Electricity-Comsumptation') ,

).properties(
    width=300,height=300,title='household06-Fridge'
).interactive()

chart7 = alt.Chart(household_data).mark_line(opacity=0.3,color='#ff7f0e').encode(
    x=alt.X('Date',title='Time[year/month/day]'),
    y=alt.Y('TAP26',title='Kettle-Electricity-Comsumptation') ,

).properties(
    width=300,height=300,title='household06-Kettle '
).interactive()

#chart8 = alt.Chart(household_data).mark_line(opacity=0.3,color='#ff7f86').encode(
 #   x=alt.X('Date',title='Time[year/month/day]'),
  #  y=alt.Y('TAP27',title='Kettle-Electricity-Comsumptation') ,

#).properties(
 #   width=300,height=300,title='household06-Kettle'
#).interactive()

    #.properties(
   # selection=interval
#)
chartS1=chart1|chart2|chart3|chart4
chartS1.save('demo1.html')
chartS2=chart5|chart6|chart7
chartS2.save('demo2.html')