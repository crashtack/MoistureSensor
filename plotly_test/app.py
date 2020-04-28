import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(y=[2,3,1]))
dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
