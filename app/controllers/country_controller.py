from flask import request
from flask_restx import Resource

from app.utils.dto import CountryDto
from app.services.country_service import save_country_population, get_all_countries

api = CountryDto.api
_country = CountryDto.country


@api.route('/')
class UserList(Resource):
    @api.doc('Update country population data')
    @api.doc(responses={201: 'Population data downloaded successfully'})
    @api.doc(responses={500: 'Internal Server error'})
    def post(self):
        return save_country_population()
    
    @api.doc(responses={500: 'Internal Server error'})
    @api.marshal_list_with(_country)
    def get(self):
        return get_all_countries()

