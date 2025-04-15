import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

st.set_page_config(layout="wide")

table_data = [
    {"Type": "Solar", "Parent": "Renewables", "Description": "Solar energy is harnessed from the sun's rays."},
    {"Type": "Wind", "Parent": "Renewables", "Description": "Wind energy is generated from the movement of air."},
    {"Type": "Geothermal", "Parent": "Renewables"},
    {"Type": "Hydropower", "Parent": "Renewables"},
    {"Type": "Rooftop Solar", "Parent": "Solar"},
    {"Type": "Covered(Parking) Solar", "Parent": "Solar"},
    {"Type": "Ground Mount Solar", "Parent": "Solar"},
    {"Type": "Field-Mounted Wind", "Parent": "Wind"},
    {"Type": "Offshore Wind", "Parent": "Wind"},
    {"Type": "Building-Mounted Wind", "Parent": "Wind"},
    {"Type": "Distributed Wind", "Parent": "Wind"},
    {"Type": "Consumer Home", "Parent": "Rooftop Solar"},
    {"Type": "Commercial", "Parent": "Rooftop Solar"},
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
        "Consumer Home": "Solar panels installed on individual homes.",}


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
