import csv
import matplotlib.pyplot as plt

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key : value for key, value in iterable}
      data.append(country_dict)
    return data

def country(data):
  Country = 'Argentina'
  Population = []
  P2022 = 0
  P2020 = 0
  P2015 = 0
  P2010 = 0
  P2000 = 0
  P1990 = 0
  P1980 = 0
  P1970 = 0
  for k in data:
    if k['Country/Territory'] == Country:
      P2022 = k['2022 Population']
      Population.append(P2022)
      P2020 = k['2020 Population']
      Population.append(P2020)
      P2015 = k['2015 Population']
      Population.append(P2015)
      P2010 = k['2010 Population']
      Population.append(P2010)
      P2000 = k['2000 Population']
      Population.append(P2000)
      P1990 = k['1990 Population']
      Population.append(P1990)
      P1980 = k['1980 Population']
      Population.append(P1980)
      P1970 = k['1970 Population']
      Population.append(P1970)
      return Population

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.xticks(rotation=45);
  plt.show()    

if __name__ == '__main__':
  Years = [
    '2022 Population',
    '2020 Population',
    '2015 Population',
    '2010 Population',
    '2000 Population',
    '1990 Population',
    '1980 Population',
    '2070 Population']  
  data = read_csv('app/data.csv')
  population = country(data)
  generate_bar_chart(Years, population)