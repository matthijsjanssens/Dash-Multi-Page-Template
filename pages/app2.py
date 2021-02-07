from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from navbar import Navbar
from page import Page
from random import seed, randint
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go


class App2(Page):

    def init_model(self):
        pass

    def init_view(self) -> html.Div:
        seed(0)
        nav = Navbar()
        body = dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H2('App 2'),
                                html.P('Some information'),
                                html.H1(' '),
                                html.H2('Graph'),
                                dcc.Graph(
                                    id=self.idx('graph'),
                                    figure={
                                        'data': [
                                            {
                                                'y': [randint(1, 100) for x in range(30)],
                                                'type': 'bar'
                                            }
                                        ],
                                    },
                                ),
                                html.P('Random Seed for Graph Data Generation'),
                                dbc.Input(
                                    id=self.idx('seed'),
                                    type='number',
                                    value=0,
                                    min=0,
                                    max=100,
                                    step=1,
                                    persistence=True,
                                    persistence_type='memory'
                                ),
                            ],
                            md=12,
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
        @self.app.callback(
            Output(self.idx('graph'), 'figure'),
            Input(self.idx('seed'), 'value')
        )
        def on_seed_changed(seed_number) -> go.Figure:
            if seed_number is None:
                raise PreventUpdate
            else:
                seed(seed_number)
                fig = {
                    'data': [{'y': [randint(1, 100) for x in range(30)], 'type': 'bar'}]
                }
                return fig


app2_page = App2()
