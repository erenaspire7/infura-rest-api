class APIError(Exception):
	def __init__(self, message, status_code):
		self.message = message
		self.status_code = status_code

	def to_dict(self):
		return {
			'status': {
				'code': self.status_code,
				'message': self.message
			}
		}

