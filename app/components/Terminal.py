from dash       import (
    html, 
    dcc, 
)
from ..static   import ( 
    prompt,
)
import app.TerminalOutputController as TC

term_label = html.Label(
    id="term_label",
    form="term_input",
    children=[prompt,],
    className='font prompt_col',
)

term_input = dcc.Input(
    id="term_input",
    placeholder="",
    autoFocus=True,
    debounce=True,
    maxLength=20,
    className='font',
)

term_output_history = html.Div(
    id="term_output_history",    
    children=[html.Div([TC.GetBanner()], className='banner_init',),],
)

term_area = html.Div(
    id="term_area",
    children=[
        term_output_history,
        term_label,
        term_input,
    ],
)

