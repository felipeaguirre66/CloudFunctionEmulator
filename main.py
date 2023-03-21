import functions_framework
import json
import datetime


@functions_framework.http
def get_time(request):
    """
    Method: get
    This function returns current time.
    """
    this_time = datetime.datetime.now()
    data = {'Current time:': str(this_time)}
    return (json.dumps(data), 200)


@functions_framework.http
def is_this_year(request):
    
    """
    Method: post
    This function allows you to check to evaluate if a given number matches current year.
    """
    
    if request.method != 'POST':
        return ('Method not allowed, POST only allowed.', 405)
    else:
        try:
            data = request.get_json(silent=True)
            current_year = datetime.datetime.now().year
            
            if data['year'] == current_year:
                response_data = {'Answer':'Correct'}
            else:
                response_data = {'Answer':'Incorrect'}

            return (json.dumps(response_data), 200)
        except:
            return ('Bad request', 400)