import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from page import Page
from navbar import Navbar


class Home(Page):

    def init_model(self):
        pass

    def init_view(self) -> html.Div:
        nav = Navbar()
        body = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2('Hello'),
                                html.P(
                                    'This is a template which can be used to build multi-page dash applications'),
                                html.P(
                                    'Use the buttons in the nav bar to switch pages'),
                            ],
                        ),
                    ]
                )
            ],
            className='mt-4',
        )
        layout = html.Div([
            nav,
            body
        ])
        return layout

    def init_controller(self) -> None:
        pass


home_page = Home()
