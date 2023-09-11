import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()#fig > figura y ax > las coordenadas
  ax.bar(labels, values)
  plt.savefig(f'./images/{name}_chart.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('chartpie.png')
  plt.close()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 200, 300]
  #generate_bar_chart(labels, values)
  generate_pie_chart()