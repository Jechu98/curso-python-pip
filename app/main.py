'''
import utils
import random
import grafica_other

data = [
  {
    'Country': 'Columbia',
    'Population': 300
  },
  {
    'Country': 'Bolivia',
    'population': 300
  }
]


def run():
  keys, values = utils.get_population()
  
  print(keys, values)
  
  print(utils.A)
  
  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)
  print(result)


#Si es ejecutado desde la terminal ejecute run
#Si es ejecutado desde otro archivo no se ejecutara
if __name__ == "__main__":
  run()
'''
import utils_other
import charts
import read_csv
import pandas as pd

'''
def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country => ')

  result = utils_other.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils_other.get_population(country)
    charts.generate_bar_chart(labels, values)

    

def run2():
  data = read_csv.read_csv('./app/data.csv')
  names, per = utils_other.world_population_percentage(data)
  charts.generate_pie_chart(names, per)

def run3():
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
'''

def run4():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  '''
  df = pd.read_csv('data.csv') #dataframe
  df = df[df['Continent'] == 'Africa']#Solo quiero seleccionar los datos en donde la columna sea Sout, esto filtra

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
#----------------------------------------------- Pandas above
  charts.generate_pie_chart(countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')

  result = utils_other.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils_other.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

     
#Si es ejecutado desde la terminal ejecute run
#Si es ejecutado desde otro archivo no se ejecutara
if __name__ == "__main__":
  run4()


'''
Importar funciones o metodos especificos
from utils2 import population_by_country
from otherutils.utils3 import Person
'''