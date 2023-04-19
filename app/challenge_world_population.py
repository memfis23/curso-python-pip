import read_csv
import charts

data = read_csv.read_csv('./app/data.csv')

data_filtered = list(filter(lambda x: x['Continent'] == 'South America', data))

labels = [country['Country/Territory'] for country in data]
values = [country['World Population Percentage'] for country in data]

charts.generate_pie_chart(labels, values)