
from app.models.country import Country
from app.db import db
import requests
from app.clients.country_api_client import CountryAPIClient


def get_all_countries():
    try:
        return Country.query.all()
    except Exception as e:
        return {"message": "Internal Server error","error":str(e)}, 500

def save_country_population():
    country_client=CountryAPIClient(["name","population"])
    try:
        data=country_client.fetch_country_data()
        for country in data:
            name = country.get('name', {}).get('common') 
            population = country.get('population')
            if name and population:
                existing_country = Country.query.filter_by(country=name).first() 
                if existing_country:
                    existing_country.population = population
                else:
                    new_country = Country(country=name, population=population)
                    db.session.add(new_country)
        db.session.commit()
        return  {"message": "Population data downloaded successfully"}, 201
    except requests.exceptions.HTTPError as e:
        return {"message": "Error requesting population data","error":str(e)}, e.response.status_code
    except Exception as e:
        return {"message": "Internal Server error","error":str(e)}, 500
