from exceptions import APIError


def hex_checker(hex_value, param):
	if hex_value[0:2] != '0x':
		raise APIError(f'Not Acceptable - {param} must have "0x" prefix', 406)

	if len(hex_value) < 3 or len(hex_value) > 18:
		raise APIError(f'Not Acceptable - {param} must be between 3 and 18 characters', 406)

	if len(hex_value) > 3 and hex_value[2] == "0":
		raise APIError(f'Not Acceptable - {param} must not have leading 0s after the "0x" prefix', 406)

	try:
		int(hex_value, 16)
	except ValueError:
		raise APIError(f'Not Acceptable - {param} must be an hexadecimal value', 406)
