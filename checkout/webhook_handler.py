from django.http import HttpResponse


class StripeWh_Handler:
    """ Handle Stripe Webhook """

    def __init__(self, request):
        self.request = request

    def handle_event(self, request):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook Recived: {event["type"]}',
            status=200)