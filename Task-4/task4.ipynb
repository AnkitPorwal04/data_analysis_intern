import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Sample data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [1000, 1200, 800, 1500, 1400, 1600],
    'Profit': [400, 500, 200, 600, 550, 700]
})

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1('Sales Dashboard'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Revenue', 'value': 'Revenue'},
            {'label': 'Profit', 'value': 'Profit'}
        ],
        value='Revenue'
    ),
    dcc.Graph(id='line-plot')
])

# Define callback to update the graph based on dropdown selection
@app.callback(
    Output('line-plot', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_value):
    fig = px.line(data, x='Month', y=selected_value, title=f'{selected_value} Over Time')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
