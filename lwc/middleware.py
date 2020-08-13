from first_app.models import Join


class ReferMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, *args, **kwargs):
        ref_id = request.GET.get("ref","")
        try:
            obj = Join.objects.get(ref_id=ref_id)
        except:
            obj = None
        if obj:
            request.session['join_id_ref'] = obj.id
