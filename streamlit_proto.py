import streamlit as st
from pyvis.network import Network
import networkx as nx
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

#Page title
st.set_page_config(page_title="Energy Knowledge Graph", layout="wide")
# 3 tabs creation
tab1, tab2, tab3 = st.tabs(["Renewable Energy", "Nuclear Energy", "Deforestation"])

#Info for tab 1 (you can place your node network here)
with tab1:
    st.markdown("## Renewable Energy")
    st.markdown("This is a knowledge graph of renewable energy sources and their components.")
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
        {"Type": "Conductive Materials", "Parent": "Solar Module Components"}
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

    # assign categories & pack nodes
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

    # build edges with a uniform label
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

    # styling
    node_styles = [
        NodeStyle("Root", "#2A9D8F", "name", icon='url(https://cdn-icons-png.flaticon.com/512/4515/4515708.png)'),
        NodeStyle("Source", "#E9C46A", "name"),
        NodeStyle("Child", "#F4A261", "name"),
    ]


    edge_styles = [
        EdgeStyle("CONTAINS", caption='label', directed=True),
    ]

    # render
    st.markdown("## Renewables Knowledge graph")
    st_link_analysis(elements, "cose", node_styles, edge_styles,1200)

# Info for tab 2 (all nuclear information goes in here)
with tab2:
    st.markdown("## Nuclear Energy")
    st.markdown("This is a knowledge graph of nuclear energy processes and components.")

    # define your parent–child relationships
    table_data = [
        {"Type": "Nuclear Fission", "Parent": "Nuclear Energy"},
        {"Type": "Nuclear Reactor", "Parent": "Nuclear Fission"},
        {"Type": "Uranium-235",     "Parent": "Nuclear Fission"},
        {"Type": "U-238",           "Parent": "Uranium-235"},
        {"Type": "Plutonium-239",   "Parent": "Nuclear Fission"},
        {"Type": "Neptunium-239",   "Parent": "Plutonium-239"},
        {"Type": "U-239",           "Parent": "Neptunium-239"},
        {"Type": "U-238",           "Parent": "U-239"},
        {"Type": "Mining",          "Parent": "U-238"},
        {"Type": "Open-pit",        "Parent": "Mining"},
        {"Type": "Underground",     "Parent": "Mining"},
        {"Type": "In-situ leaching (ISL)", "Parent": "Mining"},
        {"Type": "Yellowcake (U3O8)",      "Parent": "U-238"},
        {"Type": "UO₂ → UF₄ → UF₆",        "Parent": "Yellowcake (U3O8)"},
        {"Type": "Enrichment",     "Parent": "UO₂ → UF₄ → UF₆"},
        {"Type": "Gas centrifuge",        "Parent": "Enrichment"},
        {"Type": "Gaseous diffusion",     "Parent": "Enrichment"},
        {"Type": "Laser enrichment",      "Parent": "Enrichment"},
        {"Type": "Heat (Steam)",   "Parent": "Nuclear Fission"},
        {"Type": "Turbines",       "Parent": "Heat (Steam)"},
        {"Type": "Electricity",    "Parent": "Turbines"},
        {"Type": "PUREX",          "Parent": "Nuclear Fission"},

        {"Type": "Small Modular", "Parent": "Nuclear Reactor"},
        {"Type": "Pressurized Water", "Parent": "Nuclear Reactor"},
        {"Type": "Boiling Water", "Parent": "Nuclear Reactor"},
        {"Type": "Fast Breeder", "Parent": "Nuclear Reactor"},
    ]

    # human‐readable descriptions
    description_mapping = {
        "Nuclear Energy": "Energy released from nuclear reactions dealing with the splitting of uranium or plutonium atoms inside of a nuclear reactor. Does not directly produce greenhouse gases.",
        "Nuclear Fission": "Process of splitting fissile uranium-235 or plutonium-239 atoms by neutron bombardment. Releases heat and more neutrons, sustaining a chain reaction.",
        "Nuclear Reactor": "Facility built to sustain and control nuclear chain reactions for energy generation.",
        "Uranium-235": "Fissile isotope of uranium used as primary fuel in most reactors.",
        "Plutonium-239": "Fissile isotope produced in reactors when U-238 captures neutrons; also used as reactor fuel or weapons material.",
        "Neptunium-239": "Radioactive nuclide formed by beta decay of U-239; a precursor to Pu-239.",
        "U-239": "Unstable uranium isotope formed when U-238 captures a neutron; decays to Neptunium-239.",
        "U-238": "Most abundant natural uranium isotope; not fissile but breeds Pu-239 upon neutron capture.",
        "Mining": "Extraction of uranium ore from the earth.",
        "Open-pit": "Surface mining method where uranium ore is removed via large pits.",
        "Underground": "Subsurface mining involving tunnels to reach uranium ore.",
        "In-situ leaching (ISL)": "Circulating a solvent underground to dissolve uranium and pumping it back to the surface.",
        "Yellowcake (U3O8)": "Preliminary purified uranium oxide concentrate produced from mined ore.",
        "UO₂ → UF₄ → UF₆": "Chemical conversion sequence preparing uranium for enrichment.",
        "Enrichment": "Process of increasing the proportion of U-235 in uranium.",
        "Gas centrifuge": "Enrichment method using high-speed rotors to separate isotopes based on mass.",
        "Gaseous diffusion": "Older enrichment method forcing UF₆ gas through barriers to separate isotopes.",
        "Laser enrichment": "Technique using tuned lasers to selectively ionize U-235 atoms for separation.",
        "Heat (Steam)": "Thermal energy from fission used to generate steam.",
        "Turbines": "Machines spun by steam to produce mechanical energy.",
        "Electricity": "Final electrical energy output from turbines.",
        "PUREX": "Chemical reprocessing method to separate uranium and plutonium from spent fuel."
    }

    # build unique node list
    node_names = set()
    for row in table_data:
        node_names.add(row["Type"])
        node_names.add(row["Parent"])
    node_names = list(node_names)

    # map each name → integer ID
    node_mapping = {name: idx for idx, name in enumerate(node_names, start=1)}

    # assign categories & pack nodes
    nodes_list = []
    for name, idx in node_mapping.items():
        if name == "Nuclear Energy":
            category = "Root"
        elif name in {"Nuclear Fission", "Nuclear Reactor", "Mining", "Heat (Steam)", "Turbines"}:
            category = "Source"
        else:
            category = "Child"
        nodes_list.append({
            "data": {
                "id": idx,
                "label": category,
                "name": name,
                "Description": description_mapping.get(name, "")
            }
        })

    # build edges with a uniform label
    edges_list = []
    edge_id = 100
    for row in table_data:
        edges_list.append({
            "data": {
                "id": edge_id,
                "label": "RELATES",
                "source": node_mapping[row["Parent"]],
                "target": node_mapping[row["Type"]]
            }
        })
        edge_id += 1

    elements = {"nodes": nodes_list, "edges": edges_list}

    # styling
    node_styles = [
        NodeStyle("Root",   "#e63946", "name"),
        NodeStyle("Source", "#f4a261", "name"),
        NodeStyle("Child",  "#a8dadc", "name"),
    ]
    edge_styles = [
        EdgeStyle("RELATES", caption="label", directed=True),
    ]

    # render
    st.markdown("### Nuclear Energy Knowledge Graph")
    st_link_analysis(elements, layout="cose", node_styles=node_styles, edge_styles=edge_styles, height=800)

# Info for tab 3 (all nuclear information goes in here)
with tab3:
    st.markdown("## Deforestation")
    st.markdown("This is a knowledge graph of Deforestation processes and components.")

    # define your parent–child relationships
    table_data = [
        {"Type": "Climate Change Effects", "Parent": "Environmental Impacts of Deforestation"},
        {"Type": "GHG Emissions", "Parent": "Climate Change Effects"},
        {"Type": "Amazon", "Parent": "GHG Emissions"},
        {"Type": "Congo Basin", "Parent": "GHG Emissions"},
        {"Type": "Southeast Asia", "Parent": "GHG Emissions"},
        {"Type": "Regional Climate Changes", "Parent": "Environmental Impacts of Deforestation"},
        {"Type": "Amazon", "Parent": "Regional Climate Changes"},
        {"Type": "Congo Basin", "Parent": "Regional Climate Changes"},
        {"Type": "Southeast Asia", "Parent": "Regional Climate Changes"},
        
        {"Type": "Soil Degradation", "Parent": "Environmental Impacts of Deforestation"},
        {"Type": "Soil Erosion", "Parent": "Soil Degradation"},
        {"Type": "Fertility Loss", "Parent": "Soil Degradation"},
        {"Type": "Microbial Disruption", "Parent": "Soil Degradation"},
        {"Type": "Water Retention Loss", "Parent": "Soil Degradation"},

        {"Type": "Amazon", "Parent": "Soil Degradation"},
        {"Type": "Congo Basin", "Parent": "Soil Degradation"},
        {"Type": "Southeast Asia", "Parent": "Soil Degradation"},
    ]

    # human‐readable descriptions
    description_mapping = {
    }

    # build unique node list
    node_names = set()
    for row in table_data:
        node_names.add(row["Type"])
        node_names.add(row["Parent"])
    node_names = list(node_names)

    # map each name → integer ID
    node_mapping = {name: idx for idx, name in enumerate(node_names, start=1)}

    # assign categories & pack nodes
    nodes_list = []
    for name, idx in node_mapping.items():
        if name == "Environmental Impacts of Deforestation":
            category = "Root"
        elif name in {
            "Climate Change Effects",
            "Soil Degradation"
        }:
            category = "Source"
        else:
            category = "Child"

        nodes_list.append({
            "data": {
                "id": idx,
                "label": category,
                "name": name,
                "Description": description_mapping.get(name, "")
            }
        })

    # build edges with a uniform label
    edges_list = []
    edge_id = 100
    for row in table_data:
        edges_list.append({
            "data": {
                "id": edge_id,
                "label": "RELATES",
                "source": node_mapping[row["Parent"]],
                "target": node_mapping[row["Type"]]
            }
        })
        edge_id += 1

    elements = {"nodes": nodes_list, "edges": edges_list}

    # styling
    node_styles = [
        NodeStyle("Root",   "#e63946", "name"),
        NodeStyle("Source", "#f4a261", "name"),
        NodeStyle("Child",  "#a8dadc", "name"),
    ]
    edge_styles = [
        EdgeStyle("RELATES", caption="label", directed=True),
    ]

    # render
    st.markdown("### Nuclear Energy Knowledge Graph")
    st_link_analysis(elements, layout="cose", node_styles=node_styles, edge_styles=edge_styles, height=800)