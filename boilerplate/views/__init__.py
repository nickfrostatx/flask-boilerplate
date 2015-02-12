# Add all blueprints to this function
def register_blueprints(app):
    """Register all blueprints to app"""
    
    from .public import public
    app.register_blueprint(public)

    from .private import private
    app.register_blueprint(private)
