from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status



def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # Customize the error response format
        response.data = {
            'error': True,
            'status_code': response.status_code,
            'details': response.data
        }
    else:
        # Handle non-DRF exceptions
        return Response({
            'error': True,
            'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'details': 'Internal server error'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response