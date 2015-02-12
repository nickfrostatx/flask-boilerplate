def run():
    """Run app in development environments, not to be called in production"""
    from .app import create_app
    app = create_app()
    app.config.from_envvar('BOILERPLATE_SETTINGS')
    return app.run()

def createdb():
    """Create all database relations"""
    from .app import create_app
    from .models import db
    app = create_app()
    app.config.from_envvar('BOILERPLATE_SETTINGS')
    return db.create_all(app=app)
