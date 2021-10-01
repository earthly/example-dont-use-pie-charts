import matplotlib
import matplotlib.pyplot as plt
import numpy
import pywaffle

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
    fig = plt.figure(figsize=(10.0, 10.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.pie(data, labels=labels)
    fig.savefig(output_path, bbox_inches='tight')

def plot_bar(data, labels, output_path, sort=True, reverse=False, percentage=False, format_percentage=False):
    data, labels = process_data(data, labels, sort, reverse, percentage, format_percentage)
    fig = plt.figure(figsize=(3.0, 5.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.bar(labels, data, width=0.1)
    fig.savefig(output_path, bbox_inches='tight')

def plot_horizontal_bar(data, labels, output_path, sort=True, reverse=False, percentage=False, format_percentage=False):
    data, labels = process_data(data, labels, sort, reverse, percentage, format_percentage)
    fig = plt.figure(figsize=(10.0, 3.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.barh(labels, data, height=0.1)
    fig.savefig(output_path, bbox_inches='tight')

def plot_horizontal_lollipop(data, labels, output_path, sort=True, reverse=False, percentage=False, format_percentage=False, xlabel=None, ylabel=None, title=None):
    data, labels = process_data(data, labels, sort, reverse, percentage, format_percentage)
    fig = plt.figure(figsize=(10.0, 3.0), dpi=100)
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

def plot_square_waffle(data, labels, output_path, sort=True, reverse=False, title=None):
    if sort:
        reverse = not reverse
    data, labels = process_data(data, labels, sort, reverse, False, False)
    fig = plt.figure(
        figsize=(10.0, 3.0),
        dpi=100,
        FigureClass=pywaffle.Waffle,
        starting_location='NW',
        vertical=True,
        rows=10,
        columns=10,
        values=data,
        labels=labels,
        legend={'loc': 'upper left', 'bbox_to_anchor': (1, 1)},
    )
    fig.ax.set_title(title)
    fig.savefig(output_path, bbox_inches='tight')

def plot_horizontal_box_and_whisker(data, labels, output_path, sort=True, reverse=False, percentage=False, format_percentage=False, xlabel=None, ylabel=None, title=None, whis=None):
    data, labels = process_data(data, labels, sort, reverse, percentage, format_percentage)
    fig = plt.figure(figsize=(10.0, 3.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    data = numpy.array(data, dtype=object)
    ax.boxplot(data, labels=labels, vert=False, whis=whis)
    fig.savefig(output_path, bbox_inches='tight')
