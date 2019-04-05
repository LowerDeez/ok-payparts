from django.utils.translation import ugettext_lazy as _

__all__ = (
    'MERCHANT_TYPES',
    'DEFAULT_MERCHANT_TYPE',
    'DEFAULT_PARTS_COUNT',
    'SUCCESS',
    'FAIL',
    'STATE_CHOICES',
    'LOG_CHOICES'
)


MERCHANT_TYPES = (
    ('II', 'II'),
    ('PP', 'PP'),
    ('PB', 'PB'),
    ('IA', 'IA')
)

DEFAULT_MERCHANT_TYPE = 'II'
DEFAULT_PARTS_COUNT = 2

SUCCESS = 'SUCCESS'
FAIL = 'FAIL'


STATE_CHOICES = (
    (SUCCESS, _('Success')),
    (FAIL, _('Fail'))
)

LOG_CHOICES = (
    ('payment_create', _('Creation of payment')),
    ('callback', _('Payment callback'))
)
