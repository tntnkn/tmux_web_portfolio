from dash           import (
    html, 
)
from dash_iconify   import DashIconify
import dash_mantine_components as dmc
from .Terminal      import term_area


left_tabs = html.Div(
    id='main_area',
    children=[
        dmc.Tabs(
            id="tabs",
            orientation="horizontal",
            variant="outline",
            activateTabWithKeyboard=True,
            loop=True,
            radius=0,
            children=[
                dmc.TabsList([
                    dmc.Tab("Terminal", value="terminal_tab", className='font', icon=DashIconify(icon='tabler:terminal'),),
                ]),
                dmc.TabsPanel(id='term_tab', children=[term_area,], value="terminal_tab"),
            ],
        ),
    ],
)


upper_bar_left = html.Div(
    id='upper_bar_left',
    children=[left_tabs,],
)

left_pane = html.Div(
    id='left_pane',
    children=[upper_bar_left,],
)

