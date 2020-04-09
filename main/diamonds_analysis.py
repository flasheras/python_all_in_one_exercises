# imports 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def analysis(df):
    # Explore header
    print(df.head(10))

    # Total value of all diamonds
    sum = df.price.sum()
    print("Total $ Value of Diamonds: ${:0,.2f}".format(sum))

    # Mean price
    mean = df.price.mean()
    print("Mean $ Value of Diamonds: ${:0,.2f}".format(mean))

    # Max price
    max = df.price.max()
    print("Max $ Value of Diamonds: ${:0,.2f}".format(max))

     # Min price
    min = df.price.min()
    print("Min $ Value of Diamonds: ${:0,.2f}".format(min))

    # Summarize the data
    descript = df.price.describe()
    print("carat description:")
    print(descript)

    # Description for all non numeric objects
    descript = df.describe(include='object')
    print()
    print(descript)

    # Description for all objects
    descript = df.describe(include='object')
    print()
    print(descript)


def visualize(df):
    carat = df.carat
    clarity = df.clarity
    plt.scatter(clarity, carat)
    plt.show() # You can plot or save but not at the same time.
    # plt.savefig("name.png")


def number_per_type(df):
    clarity_indexes = df['clarity'].value_counts().index.tolist()
    clarity_count = df['clarity'].value_counts().values.tolist()
    plt.bar(clarity_indexes, clarity_count)
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv('python_all_in_one_exercises/data/diamonds.csv')
    analysis(df)
    visualize(df)
    number_per_type(df)
