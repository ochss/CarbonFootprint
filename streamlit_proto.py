import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
import pandas as pd

def build_knowledge_graph(df, category):

    node_styles_df = pd.read_csv("node_styles.csv")
    node_styles = []
    for _, row in node_styles_df.iterrows():
        node_styles.append(NodeStyle(row["type"], row["color"], caption=row["caption"]))
    
    edge_styles_df = pd.read_csv("edge_styles.csv")
    edge_styles = []
    for _, row in edge_styles_df.iterrows():
        edge_styles.append(EdgeStyle(row["type"], caption=row["caption"], directed=row["directed"]))

    # filter the DataFrame for the specified category
    df = df[df["Category"] == category]

    # drop any rows that lack a Type
    df = df.dropna(subset=["Type"])

    # build lookup maps from the CSV
    desc_map      = dict(zip(df["Type"], df["Description"]))
    node_type_map = dict(zip(df["Type"], df["Node Type"]))
    edge_type_map = dict(zip(df["Type"], df["Edge Type"]))

    # collect every unique node name (Types + Parents)
    node_names = set(df["Type"]).union(df["Parent"].dropna())
    # map each name → unique integer ID
    node_mapping = {name: idx for idx, name in enumerate(sorted(node_names), start=1)}

    # build your Cytoscape‐style nodes list
    nodes_list = []
    for name, idx in node_mapping.items():
        nodes_list.append({
            "data": {
                "id": idx,
                "label":     node_type_map.get(name, "Other"),
                "node_type": node_type_map.get(name, "Other"),
                "name":       name,
                "Description": desc_map.get(name, "")
            }
        })

    # build your edges list from Parent → Type
    edges_list = []
    edge_id = max(node_mapping.values()) + 1
    for _, row in df.iterrows():
        parent = row["Parent"]
        child  = row["Type"]
        if pd.notna(parent):
            edges_list.append({
                "data": {
                    "id":    edge_id,
                    "label": edge_type_map.get(child, "Other"),
                    "source": node_mapping[parent],
                    "target": node_mapping[child]
                }
            })
            edge_id += 1

    elements = {"nodes": nodes_list, "edges": edges_list}

    st_link_analysis(
        elements,
        node_styles=node_styles,
        edge_styles=edge_styles,
        layout="cose",
    )


#Page title
st.set_page_config(page_title="Energy Knowledge Graph", layout="wide")
# 3 tabs creation
tab1, tab2, tab3 = st.tabs(["Renewable Energy", "Nuclear Energy", "Deforestation"])
df = pd.read_csv("knowledge_graph_data.csv")

#Info for tab 1 (you can place your node network here)
with tab1:
    st.markdown("## Renewable Energy")
    st.markdown("This is a knowledge graph of renewable energy sources and their components.")

    build_knowledge_graph(df, "Renewables")

# Info for tab 2 (all nuclear information goes in here)
with tab2:
    st.markdown("## Nuclear Energy")
    st.markdown("This is a knowledge graph of nuclear energy processes and components.")

    build_knowledge_graph(df, "Nuclear Energy")

# Info for tab 3 (all nuclear information goes in here)
with tab3:
    st.markdown("## Deforestation")
    st.markdown("This is a knowledge graph of Deforestation processes and components.")

    build_knowledge_graph(df, "Deforestation")