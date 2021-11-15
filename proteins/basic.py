
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from collections import deque
from pathlib import Path


class Protein(object):

    aa_df = pd.read_csv(Path(__file__).parent.parent/'data/amino_acid_properties.csv')
    aa_df = aa_df.rename(columns={"hydropathy index (Kyte-Doolittle method)": "hydropathy"})
    #  aa_df = aa_df[["1-letter code","hydropathy index (Kyte-Doolittle method)", "pI"]]
    aa_df = aa_df.set_index("1-letter code")
    aa_metrics = aa_df.to_dict("dict")

    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    def find_metric_values(self, metric="hydropathy"):
        metric_values = []
        for aa in list(self.sequence):
            metric_values.append(self.aa_metrics[metric][aa])
        return metric_values

    def calculate_sliding_window(self, metric="hydropathy", window_size=5):
        metric_values = self.find_metric_values(metric)
        window = deque([], maxlen = window_size)
        mean_values = []
        for value in metric_values:
            window.append(value)
            mean_value = np.mean(list(window))
            mean_values.append(mean_value)
        return mean_values

    def create_positions(self):
        positions = list(np.arange(len(self.sequence)))
        return positions

    def plot(self, metric="hydropathy", window_size=5):
        data = [
            go.Bar(
                x=self.create_positions(), 
                y=self.calculate_sliding_window(metric, window_size)
            )
        ]
        fig = go.Figure(data=data)
        fig.update_layout(title = self.name, template="seaborn")
        return fig


