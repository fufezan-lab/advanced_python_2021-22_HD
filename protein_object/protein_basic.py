import csv
import re
import pandas as pd
import pathlib
import plotly
import plotly.graph_objs as go
import numpy as np

class Protein (object):

    def __init__(self, protein_file_name):
        directory = pathlib.Path().resolve()
        aa_properties_path = str(directory) + "/data/amino_acid_properties.csv"
        aa_properties_path = pathlib.Path(aa_properties_path)
        print(aa_properties_path)
        self.aa_properties_df = pd.read_csv(aa_properties_path)

        # Load the File and get the sequenz
        self.protein_file_name = protein_file_name
        protein_path = str(directory) + "/data/" + protein_file_name
        self.protein_path = pathlib.Path(protein_path)
        self.sequenz = ""
        with open(self.protein_path) as input_data:
            for line in input_data:
                if line.startswith(">"):
                    a = 0
                else:
                    stripped_line = line.strip("\n")
                    #find non ASCII characters
                    stripped_line.encode().decode('ascii')
                    
                    self.sequenz += str(stripped_line)
        

        
    def get_property(self,property = "hydropathy index (Kyte-Doolittle method)"):
        
        aa_list = self.aa_properties_df["1-letter code"].tolist()
        property_list = self.aa_properties_df[property].tolist()
        property = 0
        for i in range(len(aa_list)):
            aa_count = len(re.findall(aa_list[i],self.sequenz))
            property += aa_count * property_list[i]
        return property

    def get_property_list(self,property = "hydropathy index (Kyte-Doolittle method)"):
        
        property_list = []
        for i in range(len(self.sequenz)):
            row = self.aa_properties_df.loc[self.aa_properties_df["1-letter code"] == self.sequenz[i]]
            value = row[property].tolist()
            if len(value) == 1:
                value = value[0]
            else:
                value = np.nan
            property_list.append(value)
        return property_list

    

    def plot(self, property="hydropathy index (Kyte-Doolittle method)", window_size=5):
        """Create plotly fig object.

        The title of the fig contains protein name, 
        the x axis is the amino acid position (int) and
        y axis shows the metric at each given position. 
        A windows size can be specified to average the metrics using a sliding window 

        Args:
            metric (str, optional): Is equal to the key of the metrics dictionary the class was initialized with. 
                Defaults to "hydropathy".
            window_size (int, optional): Size of the sliding window. Defaults to 5.
        """
        property_list = self.get_property_list(property)
        if window_size > len(property_list):
            window_size = 1
        property_list_averaged = []
        window_counter = 0
        property_sum = 0
        for i in range(len(property_list)):
            #print("i = "+str(i))
            #print("window_counter = "+str(window_counter))
            #print("property_sum = "+str(property_sum))            
            if window_counter < window_size:
                window_counter += 1
                property_sum += property_list[i]
            if window_counter == window_size:
                property_average = property_sum/window_size
                property_list_averaged.append(property_average)
                window_counter = 0
                property_sum = 0
        print(len(property_list_averaged))

        plot_title = str(self.protein_file_name) + " " + str(property)
        data = [
            go.Bar(
                x0=0,
                dx=window_size,
                y=property_list_averaged,

                #marker_color=self.get_property_list('hp_color')
            )
        ]

        fig = go.Figure(data=data, layout={"template": "seaborn", "title": plot_title})
        
        #fig.show()
        return fig


    def print_list(self):
        print(list(range(len(self.sequenz))))
        





