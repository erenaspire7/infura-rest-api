from flask import json
from api import app

client = app.test_client()


def test_getlatestBlockByNumber():
	response = client.get('/getLatestBlockNumber', content_type='application/json')

	data = json.loads(response.get_data(as_text=True))

	assert data['status']['code'] == 200
	assert data['data'] is not None


def test_getBlockByNumber_bad_request():
	payload = {}

	response = client.post('/getBlockByNumber', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 400


def test_getBlockByNumber_invalid_block_number():
	payload = {
		'blockNumber': 1
	}

	response = client.post('/getBlockByNumber', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 406


def test_getBlockByNumber_not_full_transaction():
	payload = {
		'blockNumber': '0x5BAD55'
	}

	response = client.post('/getBlockByNumber', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 200
	assert isinstance(data['data']['result']['transactions'][0], str)


def test_getBlockByNumber_full_transaction():
	payload = {
		'blockNumber': '0x5BAD55',
		'showFullTransaction': True
	}

	response = client.post('/getBlockByNumber', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 200
	assert isinstance(data['data']['result']['transactions'][0], dict)


def test_getTransactionByBlockNumberAndIndex_bad_request():
	payload = {}

	response = client.post('/getTransactionByBlockNumberAndIndex', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 400


def test_getTransactionByBlockNumberAndIndex_invalid_block_number():
	payload = {
		'blockNumber': '0x12345678912345678',
		'index': '0x0'
	}

	response = client.post('/getTransactionByBlockNumberAndIndex', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 406


def test_getTransactionByBlockNumberAndIndex_invalid_index():
	payload = {
		'blockNumber': '0x5BAD55',
		'index': '123'
	}

	response = client.post('/getTransactionByBlockNumberAndIndex', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 406


def test_getTransactionByBlockNumberAndIndex_success():
	payload = {
		'blockNumber': '0x5BAD55',
		'index': '0x0'
	}

	response = client.post('/getTransactionByBlockNumberAndIndex', data=json.dumps(payload),
						   content_type='application/json')

	data = json.loads(response.get_data(as_text=True))
	assert data['status']['code'] == 200
	assert data['data'] is not None
