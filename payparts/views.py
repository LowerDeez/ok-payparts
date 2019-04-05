import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from payparts.use_cases import ProcessCallbackUseCase

__all__ = (
    'PayPartsCallbackView',
)


class PayPartsCallbackView(View):
    """
    LiqPay Callback view
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        ProcessCallbackUseCase().execute(request=request, data=data.copy())
        return JsonResponse(data)