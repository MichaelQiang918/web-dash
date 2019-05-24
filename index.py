import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import app1, app2, app3

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("app3", href="/")),
        dbc.NavItem(dbc.NavLink("app1", href="/apps/app1")),
        dbc.NavItem(dbc.NavLink("app2", href="/apps/app2")),
    ],
    vertical="md",
)
app.layout = html.Div(
    id='container',
    style={
        'display': 'grid',
        'grid-template-columns': '1fr 6fr',
    },
    children=[
        dcc.Location(id='url', refresh=False),
        html.Div(
            style={
                'background': '#13dada',
            },
            children=[nav]
        ),
        html.Div(
            id='page-content',
            style={
                'background': 'aqua',
            },
        ),
    ])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return app3.layout
    if pathname == '/apps/app1':
        return app1.layout
    elif pathname == '/apps/app2':
        return app2.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
