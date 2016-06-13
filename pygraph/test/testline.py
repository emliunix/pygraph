import unittest

from pygraph import line
import numpy as np

class TestLine(unittest.TestCase):
    def test_normalize(self):
        #        
        #      __
        #    */  
        #        
        #        
        (p, m) = line.normalize((20, 10))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [1, 0],
            [0, 1]
        ], 'i')).all())
        #        
        #        
        #    *\__
        #        
        #        
        (p, m) = line.normalize((20, -10))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [1, 0],
            [0, -1]
        ], 'i')).all())
        #     _  
        #    /   
        #    *   
        #        
        #        
        (p, m) = line.normalize((10, 20))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [0, 1],
            [1, 0]
        ], 'i')).all())
        #        
        #        
        #    *   
        #    \_   
        #        
        (p, m) = line.normalize((10, -20))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [0, 1],
            [-1, 0]
        ], 'i')).all())
        #   _    
        #    \   
        #    *   
        #        
        #        
        (p, m) = line.normalize((-10, 20))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [0, -1],
            [1, 0]
        ], 'i')).all())
        #        
        #        
        #    *   
        #   _/   
        #        
        (p, m) = line.normalize((-10, -20))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [0, -1],
            [-1, 0]
        ], 'i')).all())
        #        
        # __     
        #   \*   
        #        
        #        
        (p, m) = line.normalize((-20, 10))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [-1, 0],
            [0, 1]
        ], 'i')).all())
        #        
        #        
        # __/*   
        #        
        #        
        (p, m) = line.normalize((-20, -10))
        self.assertTrue((p == np.asmatrix([20, 10], 'i')).all())
        self.assertTrue((m == np.asmatrix([
            [-1, 0],
            [0, -1]
        ], 'i')).all())
        