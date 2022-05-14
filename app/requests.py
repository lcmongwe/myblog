import urllib.request,json
# from .models import Movie

def configure_request(app):
    global api_url
    api_url = app.config['API']


def get_quotes():
    '''
    Function that gets the json response to our url request
    '''

    with urllib.request.urlopen(api_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = get_quotes_response

        
    return quotes_results  
