import random
import plot

phonetics = ["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whiskey","x-ray","yankee","zulu"]


# generates num_data points randomly along with incrementing character labels (i.e. a, b, c, ...)
def get_data(num_data=5, mu=1, sigma=0.1):
    if not (0 < num_data <= len(phonetics)):
        raise ValueError(num_data)
    data = [random.lognormvariate(mu, sigma) for _ in range(num_data)]
    labels = list(phonetics[:len(data)])
    return data, labels

if __name__ == '__main__':
    random.seed(1)
    data, labels = get_data()

    plot.plot_pie(data, labels, 'pie-chart.png')
    plot.plot_horizontal_bar(data, labels, 'horizontal-bar-chart.png')
    plot.plot_horizontal_lollipop(data, labels, 'horizontal-lollipop-chart.png')
