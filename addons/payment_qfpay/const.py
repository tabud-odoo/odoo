# Part of Odoo. See LICENSE file for full copyright and licensing details.

RETURN_URL = '/payment/qfpay/return'
WEBHOOK_URL = '/payment/qfpay/webhook'

SUPPORTED_CURRENCIES = [
    'HKD',
    'CNY',
    'USD',
    'AED',
    'EUR',
    'IDR',
    'JPY',
    'MMK',
    'MYR',
    'SGD',
    'THB',
    'CAD',
    'AUD'
]

DEFAULT_PAYMENT_METHOD_CODES = [
    'alipay',
    'alipay_hk',
    'wechat_pay',
    'unionpay',
    'fps',
    'payme',
    'card',
# Brand payment methods
    'visa',
    'mastercard',
]

PAYMENT_STATUS_MAPPING = {
    'done': ['0000'],
    'pending': ['1143', '1145', '1298'],
    'cancel': ['1142', '1181', '1263', '1264'],
    'error': ['1108', '1201', '1202', '1204', '1205', '1294', '2005'],
}

PAYMENT_METHOD_MAPPING = {
    'alipay': '801101',
    'alipay_hk': '801514',
    'wechat_pay': '800212',
    'fps': '802001',
    'payme': '805814',
    'unionpay': '800714',
    'card': '802801',
    'visa': '802801',
    'mastercard': '802801',
}
