from app    import get_app


app = get_app()
server = app.server


if __name__ == '__main__':
    app.run_server()

