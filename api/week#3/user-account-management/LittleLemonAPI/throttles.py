from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    rate = '10/day'  # Define your desired rate limit here

    def allow_request(self, request, view):
        # Implement your custom logic to allow or deny the request
        # based on the rate limit and any additional conditions
        return super().allow_request(request, view)