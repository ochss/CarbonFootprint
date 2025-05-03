# Carbon Footprint Knowledge Graph Application - README
## Overview
This project is a prototype data product designed to support analysis of carbon footprint contributors through a knowledge graph-based exploration interface. The system models key relationships among energy production methods, environmental impacts, and carbon emissions sources.

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

· Edges: Relationships between nodes (labeled mostly as RELATES currently), showing dependencies, causal chains, or conceptual associations.

Each node includes:

· id: Unique identifier
· name: Main label
· label: ("Source" or "Child") – note: this is basic and may need more expansion
· description: (Currently incomplete for many nodes)
· position: Coordinates for graph layout

## Technologies Used
· Streamlit: Web application framework
· Cytoscape.js (likely via Streamlit components): Graph visualization
· JSON: Format for graph node and edge data

## Known Limitations (for Future Development)
· Many nodes lack detailed descriptions, which limits educational and research value.
· Node typing is currently shallow (Source vs Child) and should be expanded to include semantic categories.
· Edge labels are mostly generic (RELATES) and should be refined into meaningful relationship types (e.g., CAUSES, ENABLED_BY, EMITS).
· Graph layouts could benefit from automatic arrangement (force-directed or DAG-like) for readability.
· User interactivity is minimal (no click-based expansion, filtering, or tooltips yet).

## Recommendations for Handoff
To ensure smooth continuation of the project, the next development team should consider:

1. Enhance metadata
Expand node descriptions.
- Assign proper semantic types to nodes (e.g., Energy Source, Process, Impact).
Refine edge labels to show more specific relationships.
2. Improve visualization
- Apply automatic graph layouts for clarity.
- Add hover tooltips and/or clickable detailed views for nodes.
3. Expand knowledge coverage
- Add upstream/downstream supply chains for renewables (e.g., rare earth mining for wind turbines).
- Connect carbon footprint factors across graphs (e.g., deforestation's impact on energy access).
4. Prepare documentation
- Keep updating this README.
- Consider writing a "User Guide" to help future users explore the graphs effectively.

## Project Structure (Prototype)
carbon_footprint_app/
├── app.py (Streamlit frontend)
├── graphs/
│   ├── renewable_energy.json
│   ├── nuclear_energy.json
│   └── deforestation_impacts.json
├── README.md (this document)
└── requirements.txt (Streamlit and dependencies)

## Closing Notes
This project is intended to help data science students explore not just datasets, but structured relationships and causal pathways involved in carbon footprint estimation.
By building this as a modular knowledge graph system, it becomes possible to expand horizontally (more nodes) and vertically (more depth per node) over time, leading to a powerful educational and analytical tool.
Known Issues and Challenges
Make a list here with enough details to have the new team get started on right away.


