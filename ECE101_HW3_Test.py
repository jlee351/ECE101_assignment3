'''
Created on Aug 3, 2015

@author: rafoakwa
@note:
How to compile this file
    1. Run python3
    2. import py_compile
    3. py_compile.compile('ECE101_HWX_Test.py')
How to run the binary
    pytho3 ECE101_HWX_Test.pyc
'''
import sys
import unittest
from io import StringIO
import ECE101_HW3
from types import FunctionType
import copy
import inspect

class Testing( unittest.TestCase ):
    
    size = 4
    # Create an arbitrary "db" of the correct size
    db = list(range(size))

    def test_num_of_required_methods( self ):
        methods = [ 'createDatabase', 'displayDatabase',
                    'myMain', 'randomNumberGenerator',
                    'searchDatabase' ]
        implemented_methods = [method
                               for method in methods
                               if hasattr(ECE101_HW3, method)]
                                  
        self.assertCountEqual(implemented_methods, methods,
                         "not all required methods were implemented")

    def test_createDatabase( self ):
        if hasattr(ECE101_HW3, "createDatabase"):
            # Check number of input arguments
            fun_args = inspect.getargspec( ECE101_HW3.createDatabase )
            fun_args = len( fun_args[0] )
            self.assertEqual( fun_args, 1 )

            # check output type
            db = ECE101_HW3.createDatabase ( Testing.size )
            db_type = type( db )
            self.assertEqual( db_type, list )

            # Check lenght of database
            db_len = len( db )
            self.assertEqual ( db_len, Testing.size )

            # Check display string
            self.assertEqual( sys.stdout.getvalue(),
                              'Generating ' + str(Testing.size) +
                              ' random integers between 1 and 100\n' +
                              'Done generating random integers!\n' )
        else: self.fail( 'createDatabase function not implemented' )

    def test_displayDatabase(self):
        if hasattr(ECE101_HW3, "displayDatabase"):
            # Check number of input arguments
            fun_args = inspect.getargspec( ECE101_HW3.displayDatabase )
            fun_args = len( fun_args[0] )
            self.assertEqual( fun_args, 1 )

            # Check displpay string
            t_str = 'Values in database\n'
            for i, val in enumerate( Testing.db ) :
                t_str += 'data[' + str(i) + '] = ' + str(val) + '\n'
            ECE101_HW3.displayDatabase( Testing.db )
            self.assertEqual( sys.stdout.getvalue(), t_str )
        else: self.fail( 'displayDatabase function not implemented' )

    def test_searchDatabase(self):
        if hasattr(ECE101_HW3, "searchDatabase"):
            # Check number of input arguments
            fun_args = inspect.getargspec( ECE101_HW3.searchDatabase )
            fun_args = len( fun_args[0] )
            self.assertEqual( fun_args, 2 )

            sr = ECE101_HW3.searchDatabase ( Testing.db, Testing.db[2] )

            # Check correct output
            self.assertEqual( sr, [True, 2] )

            # Check wrong output (-1 will never be in the db)
            sr = ECE101_HW3.searchDatabase ( Testing.db, -1 )
            self.assertEqual( sr[0], False )
        else: self.fail( 'searchDatabase function not implemented' )

# Enable buffer to retrieve std.out
unittest.main(module=__name__, buffer=True, verbosity=9)
