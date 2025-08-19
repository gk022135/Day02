from home.models import RequestLog

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process request before view
        response = self.get_response(request)

        # Save log to DB after response is generated
        try:
            RequestLog.objects.create(
                request_log = request.path,        # the URL path
                request_method = request.method,   # GET/POST/etc.
                request_type = request.META.get("CONTENT_TYPE", ""), # request type (e.g. JSON, form-data)
            )
        except Exception as e:
            # Prevent logging errors from breaking the app
            print("Logging failed:", e)

        return response
