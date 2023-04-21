from dash       import (
    Output, 
    Input,
    State,
    html, 
    callback, 
    no_update,
)
import app.TerminalOutputController as TC


@callback(
    Output("tabs", "value"), 
    Output("editor_tabs", "value"), 
    Input("dummy_store", "data"),
)
def activate_default_tab(active):
    return 'terminal_tab', 'readme_tab'


@callback(
    Output("term_output_history", "children", allow_duplicate=True),
    Output("term_input", "value", allow_duplicate=True),
    Input("term_input", "value"),
    State("term_output_history", "children"),
    prevent_initial_call=True, 
)
def update_term_input_store(inp, term_out_cont):
    term_out_patch = TC.GetPatch(inp)
    return term_out_patch, ''

