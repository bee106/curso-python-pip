import matplotlib.pyplot as plt
import csv


path = '/home/bee/Documents/dev_bee/Git_bee/charts/world_population.csv'
def get_diccionari(data):
    result = {item['Country']:item['World Population Percentage'] for item in data }
    keys = result.keys()
    values = result.values()
    return keys,values


def generate_pie_chart(labels,values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig('.pie.png')
    plt.close()

def run():

    with open(path,'r') as file:
        csv_reader = csv.DictReader(file)
        labels,values = get_diccionari(csv_reader)
        print(list(labels), list(values))
        generate_pie_chart(labels,values)


if __name__ == '__main__':
    run()


