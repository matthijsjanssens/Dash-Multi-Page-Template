import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink('App 1', href='/app1')),
            dbc.NavItem(dbc.NavLink('App 2', href='/app2')),
        ],
        brand='Multi-Page Dash Template',
        brand_href='/',
        sticky='top',
        color='primary',
        dark=True
    )
    return navbar
