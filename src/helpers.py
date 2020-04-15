import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd

def plot_img_by_obj(img):
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))


def plot_img_by_path(path):
    img = cv.imread(path)
    plot_img_by_obj(img)


def describe_img(img):
    print('Type: {}'.format(type(img)))
    shape = img.shape
    print('Width: {}'.format(shape[0]))
    print('High: {}'.format(shape[1]))
    try:
        print('Dimensions/Colors: {}'.format(shape[2]))
    except:
        print('Dimensions/Colors: 1')
    print('Colors Level: {} - {}'.format(np.min(img), np.max(img)))


def plot_hist(img):
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    hist = hist.astype(int)
    hist = [h[0] for h in hist]

    df = pd.DataFrame(hist, columns=["freq"])
    df["level"] = df.index

    fig = px.bar(df, x="level", y="freq")
    fig.show()
