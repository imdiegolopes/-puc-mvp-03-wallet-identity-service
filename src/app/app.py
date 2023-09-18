# from src.application.handlers.mood_handler import MoodHandler
from handlers.exchange_rate_handler import ExchangeRateHandler
from handlers.healthcheck_handler import HealthcheckHandler
from flask import (
    Flask
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule('/', 'index', HealthcheckHandler.handle, methods=['GET'])
# app.add_url_rule('/v1/exchange-rates', 'exchange_rates',
#                  ExchangeRateHandler.handle_get_exchange_rates, methods=['GET'])
# app.add_url_rule('/v1/convert', 'convert_rates',
#                  ExchangeRateHandler.handle_post_convert_rates, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, port=8082, host="0.0.0.0")
