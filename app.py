import dash
import dash_bootstrap_components as dbc



# external JavaScript files
external_scripts = [
]
# external CSS stylesheets
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    './assets'
]

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True
