import matplotlib
import matplotlib.pyplot as plt
import numpy

def sort_data(data, labels):
    sorted_pairs = sorted(zip(data, labels))
    data, labels = zip(*sorted_pairs)
    return data, labels

def process_data(data, labels, sort, reverse, percentage, format_percentage):
    if percentage and format_percentage:
        raise ValueError("only one of percentage or format_percentage can be true")
    if sort:
        data, labels = sort_data(data, labels)
    if reverse:
        data = list(reversed(data))
        labels = list(reversed(labels))
    if percentage:
        total = float(sum(data))
        data = [float(x)/total for x in data]
    return data, labels

def plot_pie(data, labels, output_path):
    fig = plt.figure(figsize=(10.0, 7.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.pie(data, labels=labels)
    fig.savefig(output_path, bbox_inches='tight')

def plot_horizontal_bar(data, labels, output_path, sort=True, reverse=False, percentage=False, format_percentage=False):
    data, labels = process_data(data, labels, sort, reverse, percentage, format_percentage)
    fig = plt.figure(figsize=(10.0, 5.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.barh(labels, data, height=0.1)
    fig.savefig(output_path, bbox_inches='tight')

def plot_horizontal_lollipop(data, labels, output_path, sort=True, reverse=False, percentage=False, format_percentage=False, xlabel=None, ylabel=None, title=None):
    data, labels = process_data(data, labels, sort, reverse, percentage, format_percentage)
    fig = plt.figure(figsize=(10.0, 7.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.set_title(title)

    ax.hlines(labels, xmin=[0]*len(data), xmax=data, alpha=0.4, lw=2, linestyle='dotted', zorder=1)
    ax.scatter(data, labels, zorder=2)

    ax.set_xlim([0,max(data)*1.1])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if percentage or format_percentage:
        ax.xaxis.set_major_formatter(matplotlib.ticker.PercentFormatter(xmax=1.0))
    fig.savefig(output_path, bbox_inches='tight')

def plot_horizontal_box_and_whisker(data, labels, output_path, sort=True, reverse=False, percentage=False, format_percentage=False, xlabel=None, ylabel=None, title=None, whis=None):
    data, labels = process_data(data, labels, sort, reverse, percentage, format_percentage)
    fig = plt.figure(figsize=(10.0, 7.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    data = numpy.array(data, dtype=object)
    ax.boxplot(data, labels=labels, vert=False, whis=whis)
    fig.savefig(output_path, bbox_inches='tight')

#def plot_waffle(data, labels, output_path, width=10, height=10, sort=True, reverse=False, xlabel=None, ylabel=None, title=None, colormap='Dark2'):
#    data, labels = process_data(data, labels, sort, reverse, True, False)
#
#    cmap = matplotlib.cm.get_cmap(colormap)
#
#    #waffle = [-1] * ()
#    waffle = numpy.zeros((height,width))
#    num_grids = height * width
#    grids_per_label = [round(x * num_grids) for x in data]
#
#    # account for rounding errors
#    while sum(grids_per_label) < num_grids:
#        i = grids_per_label.index(max(grids_per_label))
#        grids_per_label[i] += 1
#    while sum(grids_per_label) < num_grids:
#        i = grids_per_label.index(max(grids_per_label))
#        grids_per_label[i] -= 1
#
#    label_i = 0
#    for row in range(height):
#        for col in range(width):
#            i = row*width + col
#            while label_i < len(labels) and grids_per_label[label_i] <= 0:
#                label_i += 1
#            if label_i >= len(labels):
#                break
#
#            waffle[row,col] = label_i
#            grids_per_label[label_i] -= 1
#
#    fig = plt.figure(figsize=(10.0, 7.0), dpi=100)
#    ax = fig.add_axes([0,0,1,1])
#    ax.set_title(title)
#    ax.set_xlabel(xlabel)
#    ax.set_ylabel(ylabel)
#
#    print(waffle)
#    ax.imshow(waffle)
#
#    for i, label in enumerate(labels):
#        color = cmap(i) # * 255 / len(labels))
#        ax.plot(0, 0, "-", color=color, label=label)
#
#    ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
#    ax.tick_params(which='both', width=0, grid_alpha=0)
#    ax.set_xticks(numpy.arange(-0.5, (width), 1), minor=True)
#    ax.set_yticks(numpy.arange(-0.5, (height), 1), minor=True)
#
#    ax.legend() #loc='center left', bbox_to_anchor=(1, 0.5))
#
#    ax.xaxis.set_ticks([])
#    ax.yaxis.set_ticks([])
#
#    #for row in range(height):
#    #    for col in range(width):
#    #        i = row*width + col
#    #        label_i = waffle[]
#    #        ax.imshow(row, col, color=cm(label_i))
#    fig.savefig(output_path, bbox_inches='tight')

