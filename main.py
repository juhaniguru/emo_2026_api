from flask import Flask, jsonify

from controllers import boroughs, payment_types, rate_codes, service_zones

app = Flask(__name__)

app.add_url_rule('/api/v1/boroughs', 'get_boroughs', boroughs.get_boroughs)
app.add_url_rule('/api/v1/payment_types', 'get_payment_types', payment_types.get_payment_types)
app.add_url_rule('/api/v1/payment_types', 'create_payment_type', payment_types.create_payment_type, methods=['POST'])

app.add_url_rule('/api/v1/payment_types/<payment_type_id>', 'get_payment_type', payment_types.get_payment_type)

app.add_url_rule('/api/v1/payment_types/<payment_type_id>', 'delete_payment_type', payment_types.delete_payment_type, methods=['DELETE'])

app.add_url_rule('/api/v1/payment_types/<payment_type_id>', 'edit_payment_type',
                                  payment_types.edit_payment_type,
                                  methods=['PATCH'])

app.add_url_rule('/api/v1/rate_codes', 'get_rate_codes', rate_codes.get_rate_codes)
app.add_url_rule('/api/v1/rate_codes/<rate_code_id>', 'get_rate_code', rate_codes.get_rate_code)
app.add_url_rule('/api/v1/rate_codes/<rate_code_id>', 'remove_rate_code', rate_codes.delete_rate_code, methods=['DELETE'])

app.add_url_rule('/api/v1/rate_codes', 'create_rate_code', rate_codes.create_rate_code, methods=['POST'])

app.add_url_rule('/api/v1/rate_codes/<rate_code_id>', 'edit_rate_code',
                                  rate_codes.edit_rate_code,
                                  methods=['PATCH'])

app.add_url_rule('/api/v1/service_zones', 'get_service_zones', service_zones.get_service_zones)


if __name__ == '__main__':
    app.run(debug=True)
