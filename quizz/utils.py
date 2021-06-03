import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 5))
    plt.title('Pontuação em Quizzes')
    plt.plot(x, y,marker='o',markersize='5')
    plt.xticks(rotation=15)
    plt.yticks([2,4,6,8,10,12,14,16,18,20])
    plt.xlabel('Data')
    plt.ylabel('Nota')
    plt.tight_layout()
    graph = get_graph()
    return graph