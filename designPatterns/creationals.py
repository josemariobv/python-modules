## SINGLETHON



## FACTORY ###

##Replace:
### funcion name, object_type, object_types for more descriptive variables
def get_object( object_type:str ) -> object:
    """
    params:
        object_type: type of boject to return
    return:
        object
    """

    object_types  =  {
        "object_name1": "object",
        "object_name2": "object"
    }

    assert  object_type  in  object_types.keys() , f"get_object: Invalid type {object_type}, valid options: {object_types.keys()}"

    return  object_types[object_type]




## BUILDER
### Example

## Example class class 
class Car():

    def __init__( self ):
        self.name  =  ""
        self.model  =  ""
        self.color  =  ""
        self.extras =  []
        

## Example builder class
class BulidCar():
    """
    This is useful in case of a complex setup of an object, you can add validations 
    and setup for configuration of the object and then return it
    """   
    def __init__( self ):

        self = Car( )


    def set_name( self, name:str ):
        """
        in this 'set_*' functions you can add the implementation to set up some optional feature or 
        something that needed a lot of default values to setup the object
        """
        self.name  =  name
        
        return self


    def set_model( self, model:str ):
        
        self.model  =  model
        
        return self


    def set_color( self, color:str ):
        
        self.color  =  color
        
        return self
    
    def set_extras( self, extras:list ):

        self.extras  =  extras

        return self
    
    def set_feature( self, feature, value ):
        """
        This is a more abstracted feature set,
        but can't implement specific funtionalities whitout* a mess of conditionals or not?????
        maybe can use a factory pattern to provide the right code impletementation for every feature 
        """

        self.__dict__[feature] = value

        return self
    

## Example usage
# myCar  =  BulidCar().set_color("blue").set_name("mariosCar").set_model("BMW")
# my2Car  =  BulidCar().set_color("blue").set_feature( "color", "red" )
# print( my2Car.__dict__ )