import json
import os

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def solutions(request):
    data = ''

    path = os.getcwd()
    parent = os.path.abspath(os.path.join(path, os.pardir))
    with open(parent + '\\react_wordle_back_end\data\db.json') as f:
        data = json.load(f)

    return Response(data["solutions"])

@api_view(['GET'])
def letters(request):
    data = ''

    path = os.getcwd()
    parent = os.path.abspath(os.path.join(path, os.pardir))
    with open(parent + '\\react_wordle_back_end\data\db.json') as f:
        data = json.load(f)

    return Response(data["letters"])


