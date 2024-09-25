from django.shortcuts import render
import json
import urllib.request
import urllib.parse


# Create your views here.
def index(request):

    error_message = ''  

    if request.method == 'POST':

        city = request.POST.get('city')   

        if city:

            base_url = 'https://api.openweathermap.org/data/2.5/weather'
            params = {'q': city, 'appid': '36f7077fbe283a57e2f8442e66adb040'}
            url = f"{base_url}?{urllib.parse.urlencode(params)}"

            try:

                data = urllib.request.urlopen(url).read()

                json_response = json.loads(data)

                response = {
                    'country_code': str(json_response['sys']['country']),
                    'coordinate': str(json_response['coord']['lon']) + ' ' + str(json_response['coord']['lat']),
                    'temp': str(json_response['main']['temp']) + 'k',
                    'pressure': str(json_response['main']['pressure']),
                    'humidity': str(json_response['main']['humidity']),
                }
            
            except:

                response = {}
                error_message = 'City not found'

        else:

            city = ''
            response = {}
            error_message = 'Empty Value for City'

    else:
        city = ''
        response = {}

    return render(request, 'index.html', {'response': response, 'city': city, 'error_message': error_message})