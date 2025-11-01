import plotly.graph_objects as go
import plotly.express as px

# Create a flowchart using Plotly
fig = go.Figure()

# Define node positions and properties
nodes = [
    # Start
    {"id": "start", "text": "User clicks Vote", "x": 5, "y": 12, "type": "start", "color": "#A5D6A7"},
    
    # Decision points (diamonds)
    {"id": "wallet_check", "text": "Wallet<br>connected?", "x": 5, "y": 10, "type": "decision", "color": "#FFEB8A"},
    {"id": "voter_check", "text": "Voter<br>registered?", "x": 5, "y": 8, "type": "decision", "color": "#FFEB8A"},
    {"id": "voted_check", "text": "Already<br>voted?", "x": 5, "y": 6, "type": "decision", "color": "#FFEB8A"},
    {"id": "candidate_check", "text": "Valid<br>candidate?", "x": 5, "y": 4, "type": "decision", "color": "#FFEB8A"},
    
    # Process steps
    {"id": "connect", "text": "Connect wallet", "x": 2, "y": 10, "type": "process", "color": "#B3E5EC"},
    {"id": "sign", "text": "Sign transaction", "x": 5, "y": 2, "type": "process", "color": "#B3E5EC"},
    {"id": "execute", "text": "Execute contract", "x": 5, "y": 0, "type": "process", "color": "#B3E5EC"},
    {"id": "update", "text": "Update state", "x": 5, "y": -2, "type": "process", "color": "#B3E5EC"},
    {"id": "emit", "text": "Emit event", "x": 5, "y": -4, "type": "process", "color": "#B3E5EC"},
    {"id": "confirm", "text": "Blockchain confirm", "x": 5, "y": -6, "type": "process", "color": "#B3E5EC"},
    {"id": "ui_update", "text": "UI success update", "x": 5, "y": -8, "type": "process", "color": "#B3E5EC"},
    
    # Error states
    {"id": "not_registered", "text": "Error:<br>Not registered", "x": 8, "y": 8, "type": "error", "color": "#FFCDD2"},
    {"id": "already_voted", "text": "Error:<br>Already voted", "x": 8, "y": 6, "type": "error", "color": "#FFCDD2"},
    {"id": "invalid_id", "text": "Error:<br>Invalid ID", "x": 8, "y": 4, "type": "error", "color": "#FFCDD2"},
    
    # End states
    {"id": "success", "text": "Vote recorded", "x": 5, "y": -10, "type": "success", "color": "#A5D6A7"},
    {"id": "end", "text": "End", "x": 8, "y": 2, "type": "end", "color": "#A5D6A7"},
]

# Add nodes to the plot
for node in nodes:
    if node["type"] == "decision":
        # Diamond shape for decisions
        fig.add_trace(go.Scatter(
            x=[node["x"]], y=[node["y"]], 
            mode='markers+text',
            marker=dict(size=40, symbol='diamond', color=node["color"], line=dict(width=2, color='#333')),
            text=node["text"], textposition='middle center',
            textfont=dict(size=9, color='#333'),
            showlegend=False,
            hoverinfo='skip'
        ))
    elif node["type"] in ["start", "end", "success"]:
        # Rounded rectangles for start/end
        fig.add_trace(go.Scatter(
            x=[node["x"]], y=[node["y"]], 
            mode='markers+text',
            marker=dict(size=35, symbol='circle', color=node["color"], line=dict(width=2, color='#333')),
            text=node["text"], textposition='middle center',
            textfont=dict(size=9, color='#333'),
            showlegend=False,
            hoverinfo='skip'
        ))
    else:
        # Rectangles for processes and errors
        fig.add_trace(go.Scatter(
            x=[node["x"]], y=[node["y"]], 
            mode='markers+text',
            marker=dict(size=35, symbol='square', color=node["color"], line=dict(width=2, color='#333')),
            text=node["text"], textposition='middle center',
            textfont=dict(size=9, color='#333'),
            showlegend=False,
            hoverinfo='skip'
        ))

# Define connections
connections = [
    ("start", "wallet_check"),
    ("wallet_check", "connect", "No"),
    ("connect", "wallet_check"),
    ("wallet_check", "voter_check", "Yes"),
    ("voter_check", "not_registered", "No"),
    ("voter_check", "voted_check", "Yes"),
    ("voted_check", "already_voted", "Yes"),
    ("voted_check", "candidate_check", "No"),
    ("candidate_check", "invalid_id", "No"),
    ("candidate_check", "sign", "Yes"),
    ("sign", "execute"),
    ("execute", "update"),
    ("update", "emit"),
    ("emit", "confirm"),
    ("confirm", "ui_update"),
    ("ui_update", "success"),
    ("not_registered", "end"),
    ("already_voted", "end"),
    ("invalid_id", "end"),
]

# Create node lookup
node_lookup = {node["id"]: node for node in nodes}

# Add connection lines
for conn in connections:
    start_node = node_lookup[conn[0]]
    end_node = node_lookup[conn[1]]
    
    # Add arrow line
    fig.add_trace(go.Scatter(
        x=[start_node["x"], end_node["x"]], 
        y=[start_node["y"], end_node["y"]],
        mode='lines',
        line=dict(color='#333', width=2),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add label if provided
    if len(conn) > 2:
        mid_x = (start_node["x"] + end_node["x"]) / 2
        mid_y = (start_node["y"] + end_node["y"]) / 2
        fig.add_trace(go.Scatter(
            x=[mid_x], y=[mid_y],
            mode='text',
            text=conn[2],
            textfont=dict(size=8, color='#333'),
            showlegend=False,
            hoverinfo='skip'
        ))

# Update layout
fig.update_layout(
    title="Smart Contract Voting Process",
    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
    plot_bgcolor='white',
    showlegend=False
)

# Save the chart
fig.write_image("voting_flowchart.png")
fig.write_image("voting_flowchart.svg", format="svg")
print("Chart saved successfully")