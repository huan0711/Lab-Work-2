from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot_view(request):
    # Generate plot
    x = [10,20,30,40,50]
    y = [10,20,30,40,50]
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('WORK SECOND PART')
    
    # Convert plot to base64 for embedding in HTML
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return render(request, 'plotapp/plot.html', {'plot_data': plot_data})