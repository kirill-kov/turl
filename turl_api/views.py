from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


class TurlAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    parser_classes = [FormParser, JSONParser]

    def get(self, request):
        return Response({'1': 'hello api'})

    def post(self, request):
        return Response({'2': request.data})
