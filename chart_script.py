import plotly.graph_objects as go
import numpy as np

# Since Mermaid service is unavailable, I'll create a Plotly network diagram
# to represent the decentralized voting system architecture

# Define nodes with their positions and properties
nodes = {
    'Voter Browser': {'pos': (0, 4), 'color': '#B3E5EC', 'layer': 'User'},
    'MetaMask Wallet': {'pos': (2, 4), 'color': '#B3E5EC', 'layer': 'User'},
    'Election Admin': {'pos': (0, 6), 'color': '#9FA8B0', 'layer': 'Admin'},
    'React Frontend': {'pos': (4, 5), 'color': '#A5D6A7', 'layer': 'Frontend'},
    'Web3.js Integration': {'pos': (6, 5), 'color': '#A5D6A7', 'layer': 'Frontend'},
    'Smart Contract': {'pos': (8, 5), 'color': '#FFCDD2', 'layer': 'Blockchain'},
    'Voter Registry': {'pos': (10, 6), 'color': '#FFCDD2', 'layer': 'Blockchain'},
    'Vote Storage': {'pos': (10, 5), 'color': '#FFCDD2', 'layer': 'Blockchain'},
    'Vote Counter': {'pos': (10, 4), 'color': '#FFCDD2', 'layer': 'Blockchain'},
    'IPFS Storage': {'pos': (4, 2), 'color': '#FFEB8A', 'layer': 'Storage'}
}

# Define connections with labels
connections = [
    ('Voter Browser', 'MetaMask Wallet', 'Connect'),
    ('Election Admin', 'React Frontend', 'Manage'),
    ('MetaMask Wallet', 'React Frontend', 'Auth'),
    ('React Frontend', 'Web3.js Integration', 'Interface'),
    ('Web3.js Integration', 'Smart Contract', 'Transaction'),
    ('Smart Contract', 'Voter Registry', 'Register'),
    ('Smart Contract', 'Vote Storage', 'Store'),
    ('Smart Contract', 'Vote Counter', 'Count'),
    ('React Frontend', 'IPFS Storage', 'Metadata'),
    ('IPFS Storage', 'Smart Contract', 'Hash'),
    ('Vote Counter', 'React Frontend', 'Results'),
    ('React Frontend', 'Voter Browser', 'Display')
]

# Create the plot
fig = go.Figure()

# Add connections (edges)
for start, end, label in connections:
    x0, y0 = nodes[start]['pos']
    x1, y1 = nodes[end]['pos']
    
    # Add edge line
    fig.add_trace(go.Scatter(
        x=[x0, x1, None], 
        y=[y0, y1, None],
        mode='lines',
        line=dict(color='#333333', width=2),
        hoverinfo='none',
        showlegend=False
    ))
    
    # Add arrow
    mid_x, mid_y = (x0 + x1) / 2, (y0 + y1) / 2
    angle = np.arctan2(y1 - y0, x1 - x0)
    arrow_x = mid_x + 0.2 * np.cos(angle)
    arrow_y = mid_y + 0.2 * np.sin(angle)
    
    fig.add_annotation(
        x=arrow_x, y=arrow_y,
        ax=mid_x, ay=mid_y,
        arrowhead=2, arrowsize=1, arrowwidth=2,
        arrowcolor='#333333',
        showarrow=True,
        text='',
        hovertext=label
    )

# Add nodes
for name, props in nodes.items():
    x, y = props['pos']
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(
            size=40,
            color=props['color'],
            line=dict(width=2, color='#13343B')
        ),
        text=name,
        textposition="middle center",
        textfont=dict(size=10, color='#13343B'),
        hoverinfo='text',
        hovertext=f"{name}<br>Layer: {props['layer']}",
        name=props['layer'],
        showlegend=True
    ))

# Update layout
fig.update_layout(
    title="Decentralized Voting System Architecture",
    showlegend=True,
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.05, 
        xanchor='center', 
        x=0.5
    ),
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor='white',
    annotations=[
        dict(text="Data flows from user interaction through blockchain to storage",
             x=5, y=0.5, showarrow=False, font=dict(size=12))
    ]
)

# Remove duplicate legend entries
legend_names = []
for trace in fig.data:
    if hasattr(trace, 'name') and trace.name not in legend_names:
        legend_names.append(trace.name)
        trace.showlegend = True
    else:
        trace.showlegend = False

# Save the chart
fig.write_image("voting_system_architecture.png")
fig.write_image("voting_system_architecture.svg", format="svg")

print("Decentralized Voting System Architecture chart saved successfully!")