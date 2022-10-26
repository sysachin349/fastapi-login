class auth():
    def authenticate(request):
        return request.cookies.get("user")
        