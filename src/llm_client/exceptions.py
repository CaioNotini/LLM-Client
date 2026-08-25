class LLMError(Exception):
    """Base class for exceptions in this module."""
    

class LLMConnectionError(LLMError):
    """Exception raised for errors in the connection to the LLM provider."""
    

class LLMConfigError(LLMError):
    """Exception raised for errors in the configuration of the LLM client."""
    

class LLMAPIError(LLMError):
    """Exception raised for errors returned by the LLM provider's API."""
    

class LLMRateLimitError(LLMError):
    """Exception raised when the LLM provider's rate limit is exceeded."""
    
class LLMAuthenticationError(LLMError):
    """Exception raised when authentication with the LLM provider fails."""