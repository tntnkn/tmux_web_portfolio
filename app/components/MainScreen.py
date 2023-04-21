from dash           import (
    html, 
    dcc, 
)
from .LeftPane      import left_pane
from .RightPane     import right_pane


main_screen = html.Div(
    id='main_screen',
    children=[right_pane, left_pane],
)

footer_contents = html.Div(
    id='footer_contents',
    children=[
      html.Div(
        className='footer_one',
        children=[
            html.Span(['[tmux-web]'], className='footer_one_one'),
            html.Span(['*portfolio'], className='footer_one_two'),
      ],),
      html.Div(
        className='footer_two',
        children=[
            html.Span(['made by'], className='footer_two_one'),
            html.Span(['tonotonokon'], className='footer_two_two'),
      ],),
])

footer = html.Footer(
    id='footer',
    children=[footer_contents],
)

dummy_store = dcc.Store(
    id="dummy_store",
)

term_input_store = dcc.Store(
    id="term_input_store",
    data=[],
)

