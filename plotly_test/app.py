import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

from db_read import create_connection, get_last_num_rows, create_plot_data

def get_data():
    table = "moisture_data"
    db = "/home/pi/Projects/MoistureSensor/sensorsData.db"

    conn = create_connection(db)
    with conn:
        rows = get_last_num_rows(conn, table, 5000)

    return create_plot_data(rows)

def create_fig(time, data):
    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=data, mode='lines', name='lines'))

    return fig


timestamp, temp, hum = get_data()
fig1 = create_fig(timestamp, hum)
fig2 = create_fig(timestamp, temp)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dave',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='''Dash: A web application framework for Python.''',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Input(id='my-id', value='initial value', type='text'),
    html.Div(id='my-div'),

    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2)
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
