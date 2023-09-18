
from flask import (
    jsonify, 
    request
)
import requests

baseUrl = "https://open.er-api.com"

class ExchangeRateHandler:

    def __init__(self):
        pass

    def handle_get_exchange_rates():
        currency = request.args.get('currency')

        # Check if 'currency' parameter is provided
        if currency is None or currency == "" or len(str(currency)) < 3:
            currency = "BRL"

        response = requests.get(baseUrl + "/v6/latest/" + currency)

        if response.status_code == 200:
            output = response.json()

            return jsonify({
                "source_currency": output["base_code"],
                "rates": output["rates"]
            })
        else:
            return jsonify({"error": "Failed to fetch exchange rates"}), response.status_code
    

    def handle_post_convert_rates():
        body = request.get_json()

        if body is None:
            return jsonify({"error": "Invalid request body by missing any fields `source_currency`, `target_currency` or `value`"}), 400

        if "source_currency" not in body or "target_currency" not in body or "value" not in body:
            return jsonify({"error": "Invalid request body by missing any fields `source_currency`, `target_currency` or `value`"}), 400

        if body["source_currency"] == body["target_currency"]:
            return jsonify({"error": "Invalid request body by `source_currency` and `target_currency` being the same"}), 400

        if body["value"] <= 0:
            return jsonify({"error": "Invalid request body by `value` being less than or equal to 0"}), 400

        if len(body["source_currency"]) != 3 or len(body["target_currency"]) != 3:
            return jsonify({"error": "Invalid request body by `source_currency` or `target_currency` having an invalid length"}), 400

        response = requests.get(baseUrl + "/v6/latest/" + body["source_currency"])

        if response.status_code == 200:
            response = response.json()

            output = {
                "converted_value": response["rates"][body["target_currency"]] * body["value"],
                "source_value": body["value"],
                "target_currency": body["target_currency"],
                "source_currency": body["source_currency"],
            }

            return jsonify(output)
        else:
            return jsonify({"error": "Failed to fetch exchange rates"}), response.status_code
