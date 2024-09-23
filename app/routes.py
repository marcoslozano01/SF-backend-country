from app.controllers.country_controller import api as country_ns

def configure_routes(api):
    api.add_namespace(country_ns,path="/api/v1/data/country")