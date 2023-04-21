def get_app():
    from dash       import Dash
    from .layout    import layout

    dashapp = Dash(
        __name__,
        meta_tags=[
            {"name": "viewport", "content": "width=device-width, initial-scale=1"},
        ],
    )
    dashapp.title = "tntnkn's website"
    dashapp.layout = layout
    import app.callbacks

    return dashapp

