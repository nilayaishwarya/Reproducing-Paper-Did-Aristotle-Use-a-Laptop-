import json
import os
import re

# In[250]:


def load_metrics(p, id):
    file = open(p)
    data = json.load(file)
    return data
    
def print_metric(id, metric):
    print(id)
    print(metric['validation_accuracy'])
    print(metric['validation_loss'])


# In[251]:


def load_metrics_from_path(path):
    metrics = []
    paths = os.listdir(path)
    metrics_paths = {}
    for p in paths:
        match = re.search("metrics_epoch_(.*).json", p)
        if match:
            id = int(match.group(1))
            metrics_paths[id] = path+p

    for id in sorted(metrics_paths):
        metric = metrics_paths[id]
        metrics.append(load_metrics(metric, id))
        #print_metric(id, metrics[id])
    return metrics


# In[252]:




# In[253]:


from pylab import *

def plot_metrics(paths):
    metrics = []
    for path, label in paths:
        metrics.append({'label': label, 'data': load_metrics_from_path(path)})
    
    figure, axis = plt.subplots(2, 2, figsize=(15, 10))
    
    for metric in metrics:
        axis[0,0].plot([m['training_loss'] for m in metric['data']], label=metric['label'])

    xlabel('Epoch')
    ylabel('Value')
    axis[0,0].set_title('Training loss')
    axis[0,0].legend()
    axis[0,0].grid(True)
    # show()

    for metric in metrics:
        axis[0,1].plot([m['training_accuracy'] for m in metric['data']], label=metric['label'])

    xlabel('Epoch')
    ylabel('Value')
    axis[0,1].set_title('Training accuracy')
    axis[0,1].legend()
    axis[0,1].grid(True)
    # show()
    
    for metric in metrics:
        axis[1,0].plot([m['validation_loss'] for m in metric['data']], label=metric['label'])
    
    xlabel('Epoch')
    ylabel('Value')
    axis[1,0].set_title('Validation loss')
    axis[1,0].legend()
    axis[1,0].grid(True)
    # show()

    for metric in metrics:
        axis[1,1].plot([m['validation_accuracy'] for m in metric['data']], label=metric['label'])

    # plot(t, s2)

    xlabel('Epoch')
    ylabel('Value')
    #ylim(ymin=0.55)
    axis[1,1].set_title('Validation accuracy')
    axis[1,1].legend()
    axis[1,1].grid(True)
    show()


# In[ ]:




