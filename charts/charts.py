import matplotlib.pylab as plt


def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,34,120]
    
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    #plt.show()  //muestra imagen de grafico y detiene el programa
    plt.savefig('pie.png')  #para que guarde la imagen 
    plt.close()