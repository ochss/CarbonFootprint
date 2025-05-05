import streamlit as st
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle
import pandas as pd
from pathlib import Path

# getting the node and edge styles from CSV files
node_styles_df = pd.read_csv("node_styles.csv")
node_styles = []
for _, row in node_styles_df.iterrows():
    node_styles.append(NodeStyle(row["type"], row["color"], caption=row["caption"]))
edge_styles_df = pd.read_csv("edge_styles.csv")
edge_styles = []
for _, row in edge_styles_df.iterrows():
    edge_styles.append(EdgeStyle(row["type"], caption=row["caption"], directed=row["directed"]))

def build_knowledge_graph(df, category, layout_algo):

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
                "Node Group": node_type_map.get(name, "Other"),
                "Type":       name,
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
    
    # buildings the elements dictionary for st_link_analysis
    elements = {"nodes": nodes_list, "edges": edges_list}

    # build the knowledge graph using st_link_analysis
    st_link_analysis(
        elements,
        node_styles=node_styles,
        edge_styles=edge_styles,
        layout=layout_algo
    )

# page title
st.set_page_config(page_title="Energy Knowledge Graph", layout="centered")

# sidebar legend 
with st.sidebar.expander("Node Color Legend", expanded=True):
    for ns in node_styles:
        swatch = f"""
        <span style="
          display:inline-block;
          width:12px; height:12px;
          background-color:{ns.color};
          margin-right:6px;
          vertical-align:middle;
          border:1px solid #444;
        "></span>
        """
        st.markdown(f"{swatch}{ns.label}", unsafe_allow_html=True)

# sidebar graph schema & taxonomy
with st.sidebar.expander("Knowledge Graph Schema & Taxonomy", expanded=False):
    md = Path("knowledge-graph-schema-and-taxonomy.md").read_text()
    st.markdown(md, unsafe_allow_html=True)

# graph layout algorithm selection
layout = st.selectbox(
    "Graph Layout",
    options=[
        "cose",
        "cola",
        "dagre",
        "breadthfirst",
        "grid",
        "circle",
        "concentric",
        "random"
    ],
    index=0,
    help="Choose the Cytoscape.js layout algorithm"
)

# 3 tabs creation
tab1, tab2, tab3 = st.tabs(["Renewable Energy", "Nuclear Energy", "Deforestation"])
df = pd.read_csv("knowledge_graph_data.csv")

# info for tab 1 (you can place your node network here)
with tab1:
    st.markdown("## Renewable Energy")
    st.markdown("This is a knowledge graph of renewable energy sources and their components.")
    # building the knowledge graph for Renewable Energy
    build_knowledge_graph(df, "Renewables", layout)

# info for tab 2 (all nuclear information goes in here)
with tab2:
    st.markdown("## Nuclear Energy")
    st.markdown("This is a knowledge graph of nuclear energy processes and components.")
    # building the knowledge graph for Nuclear Energy
    build_knowledge_graph(df, "Nuclear Energy", layout)

# info for tab 3 (all nuclear information goes in here)
with tab3:
    st.markdown("## Deforestation")
    st.markdown("This is a knowledge graph of Deforestation processes and components.")
    # building the knowledge graph for Deforestation
    build_knowledge_graph(df, "Deforestation", layout)