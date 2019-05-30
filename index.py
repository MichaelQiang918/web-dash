import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import app1, app2, app3

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("app3", href="/"), style={
            # 'background': '#353a48',
        }),
        dbc.NavItem(dbc.NavLink("app1", href="/apps/app1"), style={
            # 'background': '#353a48',
        }),
        dbc.NavItem(dbc.NavLink("app2", href="/apps/app2"), style={
            # 'background': '#353a48',
        }),
    ],
    vertical="md",
)
PLOTLY_LOGO = "http://adopt-web.azurewebsites.net/assets/images/signin/logo.png"
navbar = dbc.Navbar(
    [
        html.A(
            # Use row and col to control vertical alignment of logo / brand
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(dbc.NavbarBrand("GroupM", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
            ),
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
                'grid-template-columns': '1fr 5fr',
                'margin-top': '56px',
            },
            children=[
                dcc.Location(id='url', refresh=False),

                html.Div(
                    id='nav',
                    style={
                        'position': 'relative',
                        # 'background': '#353a48',
                        # 'background-image': 'url(./assets/sidebar.jpg)',
                        # 'background-repeat': 'no-repeat',
                        # 'background-position': 'center center',
                        # 'background-size': '100% 100%',
                        # 'width': '100%',
                        # 'margin': '0 auto',
                        # 'box-shadow': '0 10px 30px -12px rgba(0, 0, 0, 0.42), 0 4px 25px 0px rgba(0, 0, 0, 0.12), 0 8px 10px -5px rgba(0, 0, 0, 0.2)'
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
