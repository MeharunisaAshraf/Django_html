from django.shortcuts import redirect

def simple_middleware(get_request):

    def middleware(request):
        print(request.session.get('customer_id'))
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        #if customer is not logged in already
        if not request.session.get('customer_id'):
            return redirect(f'login?return_url={returnUrl}')
            #return redirect(f'login?return_url={returnUrl}')

        #if logged in already
        response = get_request(request)
        return response

    return middleware