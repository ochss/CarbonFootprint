import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

st.set_page_config(layout="wide")

'''
    {"Type": "Solar Uses", "Parent": "Solar"},
    {"Type": "Rooftop Solar", "Parent": "Solar Uses"},
    {"Type": "Covered(Parking) Solar", "Parent": "Solar Uses"},
    {"Type": "Ground Mount Solar", "Parent": "Solar Uses"},
    {"Type": "Consumer Home", "Parent": "Rooftop Solar Uses"},
    {"Type": "Commercial", "Parent": "Rooftop Solar Uses"},
    '''

table_data = [
    {"Type": "Solar", "Parent": "Renewables", "Description": "Solar energy is harnessed from the sun's rays."},
    {"Type": "Wind", "Parent": "Renewables", "Description": "Wind energy is generated from the movement of air."},
    {"Type": "Geothermal", "Parent": "Renewables"},
    {"Type": "Hydropower", "Parent": "Renewables"},

    

    {"Type": "Field-Mounted Wind", "Parent": "Wind"},
    {"Type": "Offshore Wind", "Parent": "Wind"},
    {"Type": "Building-Mounted Wind", "Parent": "Wind"},
    {"Type": "Distributed Wind", "Parent": "Wind"},

    

    {"Type": "Photovoltaic Cells", "Parent": "Solar"},

    {"Type": "Thin-Film Cells", "Parent": "Photovoltaic Cells"},
    {"Type": "Cadmium Telluride (CdTe)", "Parent": "Thin-Film Cells"},
    {"Type": "Copper Indium Gallium Selenide (CIGS)", "Parent": "Thin-Film Cells"},
    {"Type": "Amorphous Silicon (a-Si)", "Parent": "Thin-Film Cells"},

    {"Type": "Silicon-based Cells", "Parent": "Photovoltaic Cells"},
    {"Type": "Monocrystalline Silicon", "Parent": "Silicon-based Cells"},
    {"Type": "Polycrystalline Silicon", "Parent": "Silicon-based Cells"},
    

    {"Type": "Solar Module Components", "Parent": "Solar"},

    {"Type": "Glass Cover", "Parent": "Solar Module Components"},
    {"Type": "Encapsulants", "Parent": "Solar Module Components"},
    {"Type": "Backsheet", "Parent": "Solar Module Components"},
    {"Type": "Frame", "Parent": "Solar Module Components"},
    {"Type": "Junction Box", "Parent": "Solar Module Components"},
    {"Type": "Conductive Materials", "Parent": "Solar Module Components"},


]

description_mapping = {
    "Renewables": "Renewable energy sources are naturally replenished.",
    "Solar": "Solar energy is harnessed from the sun's rays.",
    "Wind": "Wind energy is generated from the movement of air.",
    "Geothermal": "Geothermal energy is derived from the heat stored beneath the Earth's surface.",
    "Hydropower": "Hydropower energy is generated from the flow of water in rivers and dams.",
    "Rooftop Solar": "Solar panels installed on rooftops to harness solar energy.",
    "Covered(Parking) Solar": "Solar panels installed on covered parking structures.",
    "Ground Mount Solar": "Solar panels mounted on the ground.",
        
        "Field-Mounted Wind": "Wind turbines installed in open fields.",
        "Offshore Wind": "Wind turbines installed in bodies of water, typically oceans.",
        "Building-Mounted Wind": "Wind turbines installed on buildings.",
        "Distributed Wind": "Smaller wind turbines installed in various locations.",
        "Consumer Home": "Solar panels installed on individual homes.",
        "Commercial": "Solar panels installed on commercial buildings.",
        "Consumer Home": "Solar panels installed on individual homes.",
        "Photovoltaic Cells": "Devices that convert sunlight directly into electricity.",
        "Silicon-based Cells": "Photovoltaic cells made from silicon, the most common type.",
        "Thin-Film Cells": "Photovoltaic cells made from thin layers of semiconductor materials.",
        "Solar Module Components": "Components that make up solar modules, including cells and frames.",
        "Cadmium Telluride (CdTe)": "A type of thin-film solar cell made from cadmium telluride.",
        "Copper Indium Gallium Selenide (CIGS)": "A type of thin-film solar cell made from copper, indium, gallium, and selenium.",
        "Amorphous Silicon (a-Si)": "A type of thin-film solar cell made from non-crystalline silicon.",
        "Monocrystalline Silicon": "A type of silicon solar cell made from a single crystal structure.",
        "Polycrystalline Silicon": "A type of silicon solar cell made from multiple crystal structures.",
        "Glass Cover": "The protective glass layer on top of solar modules.",
        "Encapsulants": "Materials that protect solar cells from moisture and mechanical damage.",
        "Backsheet": "The rear protective layer of solar modules.",
        "Frame": "The structural frame that holds the solar module together.",
        "Junction Box": "The box that houses the electrical connections of a solar module.",
        "Conductive Materials": "Materials that conduct electricity within solar modules.",

        }


node_names = set()
for row in table_data:
    node_names.add(row["Type"])
    node_names.add(row["Parent"])
node_names = list(node_names)


node_mapping = {}
nodes_list = []
for i, name in enumerate(node_names, start=1):
    node_mapping[name] = i
   
    if name == "Renewables":
        category = "Root"
    elif name in ["Solar", "Wind", "Geothermal", "Hydropower"]:
        category = "Source"
    else:
        category = "Child"
    nodes_list.append({"data": {"id": i, "label": category, "name": name, "Description": description_mapping[name]}})

edges_list = []
edge_id = 100  
for row in table_data:
    source = node_mapping[row["Parent"]]
    target = node_mapping[row["Type"]]
    edges_list.append({"data": {"id": edge_id, "label": "CONTAINS", "source": source, "target": target}})
    edge_id += 1


elements = {
    "nodes": nodes_list,
    "edges": edges_list
}


node_styles = [
    NodeStyle("Root", "#2A9D8F", "name", icon='url(https://cdn-icons-png.flaticon.com/512/4515/4515708.png)'),
    NodeStyle("Source", "#E9C46A", "name"),
    NodeStyle("Child", "#F4A261", "name"),
]


edge_styles = [
    EdgeStyle("CONTAINS", caption='label', directed=True),
]

st.markdown("## Renewables Knowledge graph")
st_link_analysis(elements, "cose", node_styles, edge_styles,1200)
