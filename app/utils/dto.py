from flask_restx import Namespace, fields


class CountryDto:
    api = Namespace('country', description='Country related operations')
    country = api.model('country', {
        'country': fields.String(required=True, description='Country name'),
        'population': fields.String(required=False, description='Population of the country')
    })