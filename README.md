# Carbon Footprint Knowledge Graph Application - README
## Overview
This project is a prototype data product designed to support analysis of carbon footprint contributors through a knowledge graph-based exploration interface. The system models key relationships among energy production methods, environmental impacts, and carbon emissions sources. Creation of this prototype was based on research influenced by En-ROADS, a free and interactive climate simulator that was developed by the MIT Sloan Sustainability Initiative and Climate Interactive. En-ROADS: https://en-roads.climateinteractive.org/scenario.html?v=25.4.0

The application was built using Streamlit, and organizes information into three distinct knowledge graphs:

1. Renewable Energy Graph
- Focuses on renewable energy sources (solar, wind, hydro, geothermal, biomass) and their production flows.

2. Nuclear Energy Graph
- Maps the stages of nuclear energy production, from uranium mining to enrichment, fission, and electricity generation.

3. Environmental Impacts of Deforestation Graph
- Visualizes the consequences of deforestation, such as greenhouse gas (GHG) emissions, soil degradation, water retention loss, and regional climate shifts.

## Data Model
Each graph consists of:

· Nodes: Entities such as processes (e.g., "Nuclear Fission"), materials (e.g., "U-238"), regions (e.g., "Amazon"), and impacts (e.g., "GHG Emissions").

· Edges: Relationships between nodes, showing dependencies, causal chains, or conceptual associations.

Each node includes:

· id: Unique identifier
· Node Group: The group the node belongs too
· Type: The main label identifier
· Description: Description of the node

## Technologies Used
· Streamlit: Web application framework

· st-link-analysis: built on Cytoscape.js, Graph visualization

· CSV: Format for graph node and edge data

## Known Limitations (for Future Development)

· Add to user interactivity.

· Find best graph layout algorithm.

## Recommendations for Handoff
To ensure smooth continuation of the project, the next development team should consider:

1. Improve visualization
- Apply automatic graph layouts for clarity.
- Add hover tooltips and/or clickable detailed views for nodes.
2. Expand knowledge coverage
- Add upstream/downstream supply chains for renewables (e.g., rare earth mining for wind turbines).
- Connect carbon footprint factors across graphs (e.g., deforestation's impact on energy access).
3. Prepare documentation
- Keep updating this README.
- Consider writing a "User Guide" to help future users explore the graphs effectively.

## Project Structure (Prototype)
```
carbon_footprint_app/
├── streamlit_proto.py (Streamlit frontend)
├── edge_styles.csv (Edge Styles)
├── node_styles.csv (Node Styles)
├── knowledge_graph_data.csv (Knowledge Graph Source Data)
├── knowledge-graph-schema-and-taxonomy.md (Graph Schema and Taxonomy)
├── README.md (this document)
└── requirements.txt (Streamlit and dependencies)
```

## Closing Notes
This project is intended to help data science students explore not just datasets, but structured relationships and causal pathways involved in carbon footprint estimation. It also allows for the larger deconstruction of broader topics, allowing for easier calculation of the carbon footprint contribution at multiple levels.
By building this as a modular knowledge graph system, it becomes possible to expand horizontally (more nodes) and vertically (more depth per node) over time, leading to a powerful educational and analytical tool.

## Known Issues and Challenges
- The application should be epanded upon to include more resources, carbon dioxide removal, and more. Consider if there are other optimal ways to demonstrate many more knowledge graphs within the same application.
- Figuring out how to create a node hiearchy has caused the team some trouble. We can differentiate the central node and other nodes by color and size, but have not yet given it ordered structure.


