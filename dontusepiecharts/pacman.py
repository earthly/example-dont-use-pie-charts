import math
import re
import os
import pandas
import datetime
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.pyplot as plt
import numpy
import matplotlib.ticker as mtick


if __name__ == '__main__':
    fig = plt.figure(figsize=(10.0, 4.5), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    data = [90, 10]
    labels = ['pie charts that look like pacman', 'pie charts that don\'t']
    ax.pie(data, labels=labels, colors=['#eeee33', '#4f4f4f'], startangle=20,
        textprops={
            'fontsize': 20,
        },
    )
    ax.set_title('Stop using Pie Charts; Use these alternatives instead!', fontsize=40)
    fig.savefig('pacman.png', bbox_inches='tight')
