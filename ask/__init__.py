from . import alexa_io
from alexa_io import InvalidAppIdException

''' 
Setting up some nice abstractions around good object oritented code.
'''

ResponseBuilder = alexa_io.ResponseBuilder
alexa = alexa_io.VoiceHandler()
Request = alexa_io.Request
Response = alexa_io.Response
