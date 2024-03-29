from flask import Flask, request, jsonify


from openai_api import text_completion


app = Flask(__name__)


@app.route('/')
def home():
    return 'Rendered Successfully'


@app.route('/dialogflow/receiveMessages', methods=['POST'])
def esReceiveMessage():
    try:
        data = request.get_json()

        query_text = data['queryResult']['queryText']

        result = text_completion(query_text)

        if result['status'] == 1:
            return jsonify({
                'fulfillmentText': result['response']
            })
        else:
            return jsonify({
                'fulfillmentText': 'Sorry, didn't catch it. Can you say it again?'
            })
    except Exception as e:
        print(f"Error: {str(e)}")

    return jsonify(
        {
            'fulfillmentText': f'Something went wrong: {str(e)}'
        }
    )
