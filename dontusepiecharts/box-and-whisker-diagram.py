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

    # random data plus an outlier
    # data = list(numpy.random.normal(0, 1, 100)) + [10]
    # hardcoded "random" data to keep annotation locations consistent
    data = [-0.9565865524128561, -0.2128299409770595, 1.7196614155318348, -0.2417274052956246, 2.0114542845788255, 2.7484971375197973, 0.4135899374589595, -0.9593993052748363, -0.18939876155842655, -1.82098334528369, -0.7152467427691915, -1.2686092718989643, -0.5696517901799049, 0.20348242999618518, 1.0055576129934047, -0.5078465164701768, 1.3502984453491844, 1.5111161331047926, 0.23567525895306557, 0.19414106773376943, 0.32312778277483, 1.0503133373476903, 1.0671773270903142, -0.5012801839201521, -0.056339581312000946, 0.4892642280361097, -0.6804461102018624, -0.10138412629918431, 1.0403984481886173, 1.414232235375736, -0.4364517441797786, 1.386224471223507, 1.8836728520789905, 0.30076532461995303, 0.5669435778236845, 1.9310475092220418, -0.8640859650841366, 0.26491141386990247, 0.03990851232836299, 0.8914713315733995, -1.7065171792195515, -1.2291667289233175, 0.5200415909255567, 0.7079116767003937, -0.1162005230387356, 0.4696143279451965, 1.1853290809756996, 0.9570057497563544, 1.0273614864615677, 0.7008209827418994, -0.5398744572638265, -0.12000789334494756, -0.03229111909330439, 1.913621073559916, 0.5327328442867569, -0.9414801462298215, -0.6860458561440567, 1.306809535828403, 0.010883226147310465, -0.9079777638782861, -0.9711019292449631, 2.262674909386293, -0.2558290872508657, 0.39364461743582446, 2.899362877679948, -2.0511621768480843, 0.880501769988944, 0.20859882996756898, -1.0871938622505166, 1.414901712178173, -0.6684694470033177, 0.21265970723290015, 0.8030763083747103, -1.0039389519350113, -0.16827557650753247, -1.519074385915388, 0.34627251264755715, -0.6610669609579625, 0.7378862064753193, -1.8667283138964523, -0.25867847296258606, -0.8028076837303381, -1.4704488267051479, 0.36169772392889293, -0.9931376542088758, -1.7839536884523248, 1.1841519178614062, -2.784906946561266, 0.4496435949635017, 0.820157362227502, 0.42271066124838597, 1.1958072520696261, 1.5662716500265135, -0.2641227135631156, -1.155788385852454, 0.7449845924380012, 0.21167716287421906, -1.729481491875584, 0.8347834753032771, 0.6116604751340795, 10]


    # raw points plot
    fig = plt.figure(figsize=(10.0, 3.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.set_title('random normal data')
    ax.set_xlabel('index')
    ax.set_ylabel('y')
    ax.plot(data, '.')

    # label the outlier
    ax.annotate('outlier', (98, 9))

    fig.savefig('box-and-whisker-raw-data.png', bbox_inches='tight')

    # sorted points plot
    fig = plt.figure(figsize=(10.0, 3.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.set_title('sorted random normal data')
    ax.set_xlabel('index')
    ax.set_ylabel('y')
    ax.plot(sorted(data), '.')

    # label the outlier
    ax.annotate('outlier', (98, 9))

    fig.savefig('box-and-whisker-sorted-data.png', bbox_inches='tight')

    # sorted points plot with percentiles labeled.
    fig = plt.figure(figsize=(10.0, 3.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.set_title('sorted random normal data with annotations')
    ax.set_xlabel('index')
    ax.set_ylabel('y')
    ax.plot(sorted(data), '.')

    # label the outlier
    ax.annotate('outlier', (98, 9))

    # lowest 25 percent
    ax.annotate('', xy=(0, 1), xytext=(25.5, 1), xycoords='data', textcoords='data', arrowprops={'arrowstyle': '|-|'})
    ax.annotate('lowest 25 percent of data', xy=(12, 2), ha='center', va='center')

    # middle 50 percent
    ax.annotate('', xy=(25, 3), xytext=(75.5, 3), xycoords='data', textcoords='data', arrowprops={'arrowstyle': '|-|'})
    ax.annotate('middle 50 percent of data', xy=(50, 4), ha='center', va='center')

    # highest 25 percent
    ax.annotate('', xy=(75, 5), xytext=(100, 5), xycoords='data', textcoords='data', arrowprops={'arrowstyle': '|-|'})
    ax.annotate('highest 25 percent of data', xy=(87, 6), ha='center', va='center')

    fig.savefig('box-and-whisker-sorted-data-with-annotations.png', bbox_inches='tight')


    # save box plot
    fig = plt.figure(figsize=(10.0, 3.0), dpi=100)
    ax = fig.add_axes([0,0,1,1])
    ax.set_title('box plot of random data')
    ax.set_xlabel('y')
    # dont label y axis as there is only a single boxplot
    ax.axes.yaxis.set_visible(False)
    whis = 4.0 # anything outside of 4 std deviations is an outlier
    ax.boxplot(data, vert=False, labels=('',))

    ax.annotate('min value', (-2.8, 1.10), rotation=45)
    ax.annotate('25th pctl', (-0.8, 1.10), rotation=45)
    ax.annotate('mean', (0.1, 1.10), rotation=45)
    ax.annotate('75th pctl', (0.8, 1.10), rotation=45)
    ax.annotate('max value', (2.8, 1.10), rotation=45)
    ax.annotate('outlier', (9.9, 1.10), rotation=45)

    fig.savefig('box-and-whisker-diagram.png', bbox_inches='tight')
