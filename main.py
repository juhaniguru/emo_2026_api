from flask import Flask, jsonify

from controllers import boroughs, payment_types

app = Flask(__name__)

app.add_url_rule('/api/v1/boroughs', 'get_boroughs', boroughs.get_boroughs)
app.add_url_rule('/api/v1/payment_types', 'get_payment_types', payment_types.get_payment_types)
app.add_url_rule('/api/v1/payment_types', 'create_payment_type', payment_types.create_payment_type, methods=['POST'])

app.add_url_rule('/api/v1/payment_types/<payment_type_id>', 'get_payment_type', payment_types.get_payment_type)

app.add_url_rule('/api/v1/payment_types/<payment_type_id>', 'delete_payment_type', payment_types.delete_payment_type, methods=['DELETE'])

app.add_url_rule('/api/v1/payment_types/<payment_type_id>', 'edit_payment_type',
                                  payment_types.edit_payment_type,
                                  methods=['PATCH'])

if __name__ == '__main__':
    app.run(debug=True)
