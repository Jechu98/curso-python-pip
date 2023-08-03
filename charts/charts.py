import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]
    #figura y coordenadas
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    #genera la grafica y lo guarda
    plt.savefig('pie.png')
    plt.close