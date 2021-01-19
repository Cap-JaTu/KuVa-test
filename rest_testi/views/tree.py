from rest_framework.views import APIView  # pip install django-rest-framework
from rest_framework import authentication, permissions
from django.http import JsonResponse, HttpResponseBadRequest
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework import serializers
from treelib import Tree


class API(APIView):
    authentication_classes = []
    permission_classes = []
    schema = AutoSchema()
    allowed_methods = [
        'get', 'post',  # 'put', 'delete'
    ]

    @extend_schema(
        responses={200: OpenApiTypes.OBJECT},
        parameters=[
            OpenApiParameter(
                name='id',
                type=str,
                location=OpenApiParameter.PATH,
                description='Get data for',
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        raise NotImplementedError("Not yet!")

    @extend_schema(operation={
        "operationId": "manual_endpoint",
        "description": "fallback mechanism where can go all out",
        "tags": ["tree"],
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "array"
                    }
                },
            }
        },
        "responses": {
            "200": {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "array"
                        }
                    }
                },
                "description": ""
            },
        }
    })
    def post(self, request, *args, **kwargs):
        if not isinstance(request.data, list):
            # HTTP/400
            return HttpResponseBadRequest("Expecting a JSON array!")

        input = request.data

        tree = Tree(input)
        min, max = tree.get_depths()

        output_data = [min, max]

        # Note: Returning an array, need safe to be disabled
        return JsonResponse(output_data, safe=False)
