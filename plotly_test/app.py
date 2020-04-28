import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(y=[2,3,1]))


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

    dcc.Graph(figure=fig)

])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
