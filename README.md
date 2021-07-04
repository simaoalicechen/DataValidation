# DataValidation



We need to define classes that have fields taht we want validated before we can set their values. This might be because we need these objects be serialized into a database, and we need to ensure the data is valid before we write to the database. 

1. Write two data descriptors: IntegerField --> Only allows integral numbers, between minimum and maximum value CharField --> Only allows strings with a minimum and maximum length 

2. Then refactor the code and create a BaseValidator class that will handle the common functionality. 

3. Then change IntegerField and CharField descriptors to inherit from BaseValidator 

Note: You can omit one or both of the minimum and maximum values where it makes sense. 
      You may want to specify a string field that has no maximum limit. 
      Or you may want an integer field that has an upper bound, but no lower bound, or no bounds at all.
 
