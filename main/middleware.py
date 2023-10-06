# from django.http import HttpResponseForbidden
#
#
# class IPRestrictedMiddleware:
#     def __init__(self,get_response, ip_addresses):
#         self.get_response = get_response
#         self.ip_addresses = ip_addresses
#
#     def __call__(self, request ,*args, **kwargs):
#         client_ip = request.META.get('REMOTE_ADDR')
#
#         if client_ip not in self.ip_addresses:
#             return HttpResponseForbidden('Permission denied')
#
#         response = self.get_response(client_ip)
#         return response
