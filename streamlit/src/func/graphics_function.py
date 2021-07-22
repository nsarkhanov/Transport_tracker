import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.metrics import plot_confusion_matrix


def pairplot(df, title, column_name, size_column):
    g = sns.PairGrid(df, hue=column_name)
    g.map_diag(sns.histplot)
    g.map_offdiag(sns.scatterplot, size=df[size_column])
    g.add_legend(title=title, adjust_subtitles=True)


def swarmplot(df, title, size, hue_target, x_column, y_column):
    plt.figure(figsize=(size))
    sns.swarmplot(data=df, x=x_column, y=y_column,
                  hue=hue_target, palette='Set1')
    plt.xticks(rotation=90)
    plt.title(title, fontsize=14)


def hist_plot(df, title, x_column, heu_column):
    sns.histplot(data=df, x=x_column, hue=heu_column)
    plt.title(title, fontsize=14)


def box_swarm_plot(df, title, size, x_column, y_column):
    plt.figure(figsize=(size))
    sns.boxplot(data=df, x=x_column, y=y_column, palette='Pastel1')
    sns.swarmplot(data=df, x=x_column, y=y_column, palette='Set1')
    plt.title(title, fontsize=14)


def kdeplot(df, size, title, x_column, y_column, hue_target):
    plt.figure(figsize=(size))
    sns.kdeplot(data=df, x=x_column, hue=y_column, palette='Set1', fill=True)
    plt.title(title, fontsize=14)


def plot_corr(df, size, title):
    plt.figure(figsize=(size))
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='viridis', cbar=True)
    plt.title(title, fontsize=14)


def confusion_materix(model, x_test, y_test, title, size):
    plot_confusion_matrix(model, x_test, y_test, cmap=plt.cm.Blues)


def bar_plot(x_column, y_column, title):
    plt.barh(x_column, y_column, align='center', alpha=0.5)
    plt.xticks(x_column, y_column)
    plt.title(title)
