import pymongo
import logging
import time


class MongoDB:
    

    def __init__( self, connectionString:str="localhost", databaseName:str="test" ):
        """
            params:
                TODO
                connectionString
                database            
        """
        # TODO validate params
        # TODO: handle connection erros
        # TODO: set a timeout for the db connection
        self.connectionString  =  connectionString
        self.connection  =  pymongo.MongoClient(connectionString)[databaseName]



    def insert_one( self, data:dict, collection:str ) -> ( any , str | None ):
        """
        params:
            data: dictionary to write to the database
            collection: collection to write the data
        retrun:
            resource_id  ,  error 
            if unable to write to the database resource id is going to be None
            if no errors "error" should be empty
        """

        assert type(data) == dict and  data  ,  f"MongoDB.insert_one: data should be a non empty dictionary not {type(data)}:{data}"
        assert type(collection) == str  and  collection  ,  f"MongoDB.insert_one: collection should be a non empty string not {type(collection)}:{collection}"


        try:

            result  =  self.connection[ collection ].insert_one( data )

            return  result.inserted_id  ,  "" 


        except Exception as exeception:

            return  ""  ,  str(exeception.args) 

        

    def find_one( self, filters:dict,  collection:str ) -> ( any , None | str ):
        """
        params:
            filters<dict>: A dictionary used as filter to identify the database resource ex: {"name": "mario"} (will return an object that has "name" set to mario)
            collection<str>: The collection to search in
        
        return:
            data  ,  error
            if no data found data is going to be empty and error will be empty
            if no errors it is going to be an empty string
        """

        assert type(filters) == dict  ,  f"MongoDB.find_one: filters should be of type dictionary not { type(filters) }" 
        assert type(collection) == str and  collection  ,  f"MongoDB.find_one: collection should be a non empty string not {type(collection)}:{collection}"


        try:

            result  =  self.connection[ collection ].find_one( filters )
            return result  ,  ""


        except Exception as exeception:
            
            return  None  ,  str( exeception.args )



    def find( self, filters:dict,  collection:str ) -> ( any , None | str ):
        """
        params:
            filters<dict>: A dictionary used as filter to identify the database resource ex: {"name": "mario"} (will return an object that has "name" set to mario)
            collection<str>: The collection to search in
        
        return:
            data  ,  error
            if no data found data is going to be empty and error will be empty
            if no errors it is going to be an empty string
        """

        assert type(filters) == dict  ,  f"MongoDB.find: filters should be of type dictionary not { type(filters) }" 
        assert type(collection) == str  and  collection  ,  f"MongoDB.find: collection should be a non empty string not {type(collection)}:{collection}"


        try:

            result  =  self.connection[ collection ].find( filters )
            return list(result)  ,  ""


        except Exception as exeception:
            
            return  None  ,  str( exeception.args )



    def update_one( self, filters:dict, collection:str, update:dict ) -> ( any , str ):
        """
        params:
            filters<dict>: A dictionary used as filter to identify the database resource ex: {"name": "mario"} (will return an object that has "name" set to mario)
            collection<str>: The collection to search in
            update<dict>: TODO
        
        return:
            new_data  ,  error
            if no data found data is going to be empty and error will be empty
            if no errors it is going to be an empty string
        """

        assert type(filters) == dict  ,  f"MongoDB.update_one: filters should be of type dictionary and not empty, not { type(filters) }: { filters }" 
        assert type(collection) == str  and  collection  ,  f"MongoDB.update_one: collection should be a non empty string not { type(collection) }: {collection }"


        try:
        
            result = self.connection[collection].update_one( filter=filters, update=update  )
            return  result.raw_result  ,  ""
        

        except Exception as exeception:

            return None  ,  str( exeception.args )



    def update_many( self, filters:dict, collection:str, update:dict ) -> ( any , str ):
        """
        params:
            filters<dict>: A dictionary used as filter to identify the database resource ex: {"name": "mario"} (will return an object that has "name" set to mario)
            collection<str>: The collection to search in
            update<dict>: TODO
        
        return:
            new_data  ,  error
            if no data found data is going to be empty and error will be empty
            if no errors it is going to be an empty string
        """

        assert type(filters) == dict  ,  f"MongoDB.update_many: filters should be of type dictionary and not empty, not { type(filters) }: { filters }" 
        assert type(collection) == str  and  collection  ,  f"MongoDB.update_many: collection should be a non empty string not { type(collection) }: {collection }"


        try:
        
            result = self.connection[collection].update_many( filter=filters, update=update  )
            return  result.raw_result  ,  ""
        

        except Exception as exeception:

            return None  ,  str( exeception.args )



    def delete_one(self, filters:dict, collection:str ) -> ( any , str ):
        """
        params:
            filters<dict>: A dictionary used as filter to identify the database resource ex: {"name": "mario"} (will return an object that has "name" set to mario)
            collection<str>: The collection to search in
            update<dict>: TODO
        
        return:
            new_data  ,  error
            if no data found data is going to be empty and error will be empty
            if no errors it is going to be an empty string
        """

        assert type(filters) == dict  ,  f"MongoDB.delete_one: filters should be of type dictionary and not empty, not { type(filters) }: { filters }" 
        assert type(collection) == str  and  collection  ,  f"MongoDB.delete_one: collection should be a non empty string not { type(collection) }: {collection }"


        try:
        
            result = self.connection[collection].delete_one( filter=filters  )
            
            return  result.raw_result  ,  ""
        

        except Exception as exeception:

            return None  ,  str( exeception.args )



    def delete_many(self, filters:dict, collection:str ) -> ( any , str ):
        """
        params:
            filters<dict>: A dictionary used as filter to identify the database resource ex: {"name": "mario"} (will return an object that has "name" set to mario)
            collection<str>: The collection to search in
        return:
            new_data  ,  error
            if no data found data is going to be empty and error will be empty
            if no errors it is going to be an empty string
        """

        assert type(filters) == dict  ,  f"MongoDB.delete_many: filters should be of type dictionary and not empty, not { type(filters) }: { filters }" 
        assert type(collection) == str  and  collection  ,  f"MongoDB.delete_many: collection should be a non empty string not { type(collection) }: {collection }"


        try:
        
            result = self.connection[collection].delete_many( filter=filters  )
            return  result.raw_result  ,  ""
        

        except Exception as exeception:

            return None  ,  str( exeception.args )
        


    

# This decorator shuld be able to retry any function if specified and in a given amount of time
def retry_function( function ):

    def wraped_retry_function(  logger=logging.getLogger("TEST") ,validateResultFunc=is_successful, secondsBeforeRetry=1, maxRetryAttempts=0,  *args, **kwargs ):
        
        logger.info(f"{function.__name__}: parms: {kwargs}")
        
        result  =  function( *args, **kwargs )
        
        success  =  validateResultFunc( result )

        if success:
            
            return result
        
        for attempt in range( 1,  maxRetryAttempts+1 ):
            
            logger.info( f"Waiting {secondsBeforeRetry} seconds before retry {attempt}/{maxRetryAttempts}" )
            time.sleep( secondsBeforeRetry )
            logger.info( f"Retring now" )

            result  =  function( *args, **kwargs )

            if validateResultFunc( result ):

                return result
            
        return result


    return wraped_retry_function


def is_successful( result:tuple ) -> bool:
    
    error = result[1]
    
    if error:
        return False
    
    return True



def test(func,  **kwargs):
    def wtest(*args):
        print("before")

        def wwtest(*args):
            print("before 2")
            return func()


        return wwtest
    
    return wtest




@test()
def saludar( ):
    """
    params:
        logger:

    """
    print("Hola")
    return ( "hola", "g" )



if __name__ == "__main__":
    # print(
    #     MongoDB().delete_many( {"name":"marios" }, collection="TEST"  )
    # )
    logging.basicConfig( level=logging.WARNING )
    saludar(  )