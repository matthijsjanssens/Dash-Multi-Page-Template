from app import app
from dash.dependencies import Input, Output
from pages.app1 import app1_page
from pages.app2 import app2_page
from pages.home import home_page
import dash_core_components as dcc
import dash_html_components as html

server = app.server
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/' or pathname == '/home':
        return home_page.view
    elif pathname == '/app1':
        return app1_page.view
    elif pathname == '/app2':
        return app2_page.view
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
