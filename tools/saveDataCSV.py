import csv


def saveTimeSerieCSV(timeSerie):

    column_names = ['cost', 'time']
    with open('timePriceOf_BTCUSA.csv', mode = 'w', newline = '') as file:

        writer = csv.writer(file)
        writer.writerow(column_names)

        for cost, time in timeSerie:
            # print(cost, time)
            writer.writerow([cost, time])
















