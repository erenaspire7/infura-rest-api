from utils import hex_checker
from exceptions import APIError


def test_hex_checker_no_hex_prefix():
	block_number = "1"
	param = 'Block Number'
	expected_status_code = 406
	expected_message = f'Not Acceptable - {param} must have "0x" prefix'

	try:
		hex_checker(block_number, param)
	except APIError as e:
		assert e.status_code == expected_status_code
		assert e.message == expected_message


def test_hex_checker_less_than_min_characters():
	index = "0x"
	param = 'Index'
	expected_status_code = 406
	expected_message = f'Not Acceptable - {param} must be between 3 and 18 characters'

	try:
		hex_checker(index, param)
	except APIError as e:
		assert e.status_code == expected_status_code
		assert e.message == expected_message


def test_hex_checker_more_than_max_characters():
	block_number = "0x12345678912345678"
	param = 'Block Number'
	expected_status_code = 406
	expected_message = f'Not Acceptable - {param} must be between 3 and 18 characters'

	try:
		hex_checker(block_number, param)
	except APIError as e:
		assert e.status_code == expected_status_code
		assert e.message == expected_message


def test_hex_checker_leading_0s_after_hex_prefix():
	index = "0x0123"
	param = 'Index'
	expected_status_code = 406
	expected_message = f'Not Acceptable - {param} must not have leading 0s after the "0x" prefix'

	try:
		hex_checker(index, param)
	except APIError as e:
		assert e.status_code == expected_status_code
		assert e.message == expected_message
