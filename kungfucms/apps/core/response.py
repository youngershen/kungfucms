# PROJECT : kungfucms
# TIME    : 2020/6/8 10:35
# AUTHOR : Younger Shen
# EMAIL : shenyangang@163.com
# PHONE : 13811754531
# WECHAT : 13811754531
# https://github.com/youngershen
import json
from django.http.response import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


class JsonResponse(HttpResponse):
    def __init__(self, data, safe=True, encoder=DjangoJSONEncoder,
                 json_dumps_params=None, **kwargs):
        self.encoder = encoder
        if safe and not isinstance(data, dict):
            raise TypeError(
                'In order to allow non-dict objects to be serialized set the '
                'safe parameter to False.'
            )
        if json_dumps_params is None:
            json_dumps_params = {}
        kwargs.setdefault('content_type', 'application/json')
        self.data = data
        data = json.dumps(data, cls=self.encoder, **json_dumps_params)
        super().__init__(content=data, **kwargs)

    def update(self, data, **kwargs):
        self.data.update(data)
        data = json.dumps(self.data, cls=self.encoder)
        super().__init__(content=data, **kwargs)
