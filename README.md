
# pYAtlas

My simple lib for automated tests, but its a joke


# Syntax

After download just put on your project folder

## Import pYAtlas to your project

from core import pYAtlas


## Methods

pYAtlas.Test('Put a test name here','put a callback function here')

### Callback functions 
    
pYAtlas.Expect('put the expected value here').toBe('put the value who you expect to recive')


## Examples

    pYAtlas.Test('Foo',pYAtlas.Expect('Foo').toBe('Bar'))

         * Return Error

    pYAtlas.Test('Foo ',pYAtlas.Expect('Baz').toBe('Baz'))

        * Return Sucess

### Other examples

    def sum(x,y):
        return x+y

    pYAtlas.Test('Sum Function',pYAtlas.Expect(sum(2,2)).toBe(5))

        * Return Error

    pYAtlas.Test('Sum Function ',pYAtlas.Expect(sum(2,2)).toBe(4))

        * Return Sucess



