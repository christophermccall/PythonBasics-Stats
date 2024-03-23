import math
from typing import List


def zcount(data: List[float]) -> float :
    return len(data)


def zmean(data: List[float]) -> float :
    return sum(data)/zcount(data)


def zmode(data: List[float]) -> float:
    data_count = [data.count(data[i]) for i in range(len(data))]
    return data[data_count.index(max(data_count))]


def zmedian(data: List[float]) -> float:
    return zcount(data)/2


def zvariance(data: List[float]) -> float:
    deviations_squared = [(data[i] - zmean(data))**2 for i in range(len(data))]
    return sum(deviations_squared) / (zcount(data) - 1)  # the sample variance


def zstddev(data: List[float]) -> float:
    # sqrt of variance
    return math.sqrt(zvariance(data))


def zstderr(data: List[float]) -> float:
    return zstddev(data) / math.sqrt(zcount(data))


def cov(a, b):
    a_devs = [a[i] - zmean(a) for i in range(len(a))]
    b_devs = [b[j] - zmean(b) for j in range(len(b))]
    ab_dev_products = [a_devs[k] * b_devs[k] for k in range(len(a))]
    return sum(ab_dev_products) / (zcount(a)-1)


def zcorr(datax: List[float], datay: List[float]) -> float:
    return cov(datax, datay) / (zstddev(datax) * zstddev(datay))


def readDataFile(file):
    x, y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)

def readDataSets(files):
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data
