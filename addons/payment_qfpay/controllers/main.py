import hmac
import logging

from odoo import http
from odoo.http import request
from odoo.addons.payment_qfpay import const

_logger = logging.getLogger(__name__)


class QFPayController(http.Controller):

    @http.route(
        const.RETURN_URL, type='http', auth='public', methods=['GET']
    )
    def qfpay_return_from_checkout(self, **data):
        _logger.info("User returned from QFPay for transaction reference: %s", data.get('out_trade_no'))
        return request.redirect("/payment/status")

    @http.route(
        const.WEBHOOK_URL, type='http', auth='public', methods=['POST'],
        csrf=False, save_session=False
    )
    def qfpay_webhook(self, **data):
        _logger.info("QFPay webhook received with data:\n%s", data)
        reference = request.env['payment.transaction']._extract_reference('qfpay', data)
        tx_sudo = request.env['payment.transaction'].sudo().search([('reference', '=', reference)])

        if tx_sudo:
            if self._verify_signature(data, tx_sudo):
                tx_sudo._process(data)
        else:
            _logger.warning("QFPay Webhook: No transaction found for reference %s", reference)

        return "SUCCESS"

    @staticmethod
    def _verify_signature(data, tx_sudo):
        """ Verify the signature. """
        received_sign = data.get('sign')
        if not received_sign:
            _logger.warning("QFPay: Missing signature.")
            return False

        expected_sign = tx_sudo.provider_id._qfpay_generate_sign(data)
        if not hmac.compare_digest(received_sign, expected_sign):
            _logger.warning("QFPay: Invalid signature received from gateway.")
            return False
            
        return True
