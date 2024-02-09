import requests
import logging
import time

# Create a function That handles errors and logging of an http request
"""
    handles:
        logging:
            user can specify the logging level
            user can add a request id if wanted for logging
        errors:
            connection error ( time out, unable to resolve, server dont respond ) logs request params
            server response error ( unautorized, internal error ) logs request params
            corrupted response?? is this posible ( be prepared at least )**** logs request params
        features:
            can finish the process if specified
            user can specify a custom logger
            Should recevice all parameters of reqeuests.request
"""


def web_request(  logger=logging.getLogger("web_request"),  **requestKwargs  )  ->  ( requests.Response | None, str ):
    
    """
    Performs an http request and handles errors and loging. 

    Params:
        logger<logger>: A logging system that implements same methods (info, error, warning, critical ... ) as logging build in module
        requestKwArgs<kwargs>: Key value arguments to be sent to the "requests.request" method to perform the http request
    
    Return:
        This function returns two values "response" and an "error message"
        In case there are no errors an empty string wil be returned
        In case there is no server response None will be return as "response"

        Retrun structure -> ( requests.Response | None, str )
    """
     
    try:

        serverResponse  =  requests.request(**requestKwargs)

        log_web_request( serverResponse, logger=logger )
        
        error  =  check_web_request_errors( serverResponse )
        
        return serverResponse ,  error
    

    except Exception as exception:
        logger.error(
            f"""Fail to execute web_request for  { requestKwargs.get( "url", None ) }:  
                requestKwargs: { requestKwargs }
                error: { exception.args }
            """
        )
        return None, str(exception.args)


def try_web_request(  logger=logging.getLogger("web_request"),  maxRetries=0,  secondsBeforeRetry=1,  **requestKwargs  )  ->  ( requests.Response | None, str ):
    
    response , error  =  web_request( logger=logger, **requestKwargs )
        
    if not error:
        return response, error
    
    
    for attempt in range( 1, maxRetries+1 ):
        
        logging.info( f"Waiting {secondsBeforeRetry} seconds before retring" )
        time.sleep( secondsBeforeRetry )

        logger.warning( f"Retring web_request: ({attempt}/{maxRetries})" )
        response , error  =  web_request( logger=logger, **requestKwargs )
        
        if error:
            continue

        else:
            break
    

    return  response ,  error



# Create a function on top of the previous one with retry options
def log_web_request(  response:requests.Response, logger=logging.getLogger("web_request") ) -> None :
    
    assert type( response )  ==  requests.Response  ,  "log_web_request: Should receive response of type requests.Response" 
    
    is_successful = response.status_code >= 200 and response.status_code < 300

    if is_successful:
        logger_writer  =  logger.info

    else:
        logger_writer =  logger.error
    
    request:requests.Request  =  response.request
    
    logger_writer(f"""
    Request details for { request.url }:
        Headers: { request.headers } 
        Payload: { request.body }
        Method: { request.method }
    Response: 
        Headers: { response.headers }
        Payload: { response._content }
        Status Code: { response.status_code }
    """)

    return None


def check_web_request_errors( response: requests.Response ) -> str:
    """Needs to be implemented"""
    is_successful_response = response.status_code >= 200 and response.status_code < 300
    if  is_successful_response:
        return ""
    
    return f"""
            Status code ( { response.url } ) : { response.status_code } 
            response content: { response.content }
            """


def check_valid_logger( logger ) -> bool :
    #TODO: Implemenmt a logger validator that checks if it has the required methods to handle all the usage for this module

    pass




if __name__ == "__main__":
    
    logging.basicConfig( level=logging.CRITICAL )
    logger  =  logging.getLogger("TEST")
    

    try_web_request(
            url="http://localhost/testddf", 
            method="GET",
            logger=logger,
            maxRetries=1
            )






