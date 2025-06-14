import datetime



class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("RequestLoggingMiddleware: Processing request...")
        now = datetime.datetime.now()


        #Getting the user information
        user = getattr(request, 'user', None)
        if user and user.is_authenticated:
            username = user.username

        else:
            username = 'Anonymous'

        # Log the request details
        log_message = f"{now} - User: {username} - Path: {request.path}\n"
        with open('requests.log', 'a') as log_file:
            log_file.write(log_message)

        response = self.get_response(request)
        return response

