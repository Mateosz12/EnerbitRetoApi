import json
import requests
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')




    
        
def before_all(context):
    
    context.base_url = 'https://restful-booker.herokuapp.com'
    context.booking_id = None  # Inicializa el booking_id como None

def after_all(context):
    # Aquí puedes limpiar o reiniciar cualquier cosa si es necesario
    pass
   
