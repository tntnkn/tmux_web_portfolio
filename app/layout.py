from dash           import (
    html, 
)
from .components    import (
    main_screen, footer, dummy_store, 
)


layout = html.Div([
    main_screen,
    footer,
    dummy_store,
])

