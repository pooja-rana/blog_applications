from collections import OrderedDict
from rest_framework.response import Response
from rest_framework import status


class ResponseHandler:
    """ Common Http response handler methods """

    @staticmethod
    def success(
            message: str = "",
            payload: dict = {},
            headers: dict = {},
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status.HTTP_200_OK,
            status=True,
            payload=payload
        )
        response_dict.update(kwargs)
        return Response(response_dict, headers=headers)

    @staticmethod
    def bad_request(
            message: str = "",
            payload: dict = {},
            headers: dict = {},
            status_code: int = status.HTTP_400_BAD_REQUEST,
            *args,
            **kwargs
    ) -> Response:
        response_dict = OrderedDict(
            message=message,
            status_code=status_code,
            status=False,
            payload=payload
        )
        response_dict.update(kwargs)
        return Response(response_dict, status=status_code, headers=headers)
