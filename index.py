import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import app1, app2, app3

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("app3", href="/"), style={
            'background': '#353a48',
            'color': 'white',
        }),
        dbc.NavItem(dbc.NavLink("app1", href="/apps/app1")),
        dbc.NavItem(dbc.NavLink("app2", href="/apps/app2")),
    ],
    vertical="md",
)
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("WM", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
            href="https://plot.ly",
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        # dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
    ],
    color="#1f1b1b",
    dark=True,
)
app.layout = html.Div(
    id='',
    style={

    },
    children=[
        html.Div(
            id='navbar',
            style={
                'position': 'fixed',
                'width': '100%',
                'top': '0px',
            },
            children=[navbar]

        ),
        html.Div(
            id='container',
            style={
                'display': 'grid',
                'grid-template-columns': '1fr 6fr',
                'margin-top': '56px',
            },
            children=[
                dcc.Location(id='url', refresh=False),

                html.Div(
                    id='nav',
                    style={
                        'background': '#353a48',
                    },
                    children=[nav]
                ),
                html.Div(
                    id='page-content',
                    style={
                        'height': '701px',
                        'background': '#eeeeee'
                    },

                ),
            ])
    ]
)


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
    app.run_server(debug=False)
