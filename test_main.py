import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_exists(self) : 
        self.assertTrue( S2 in globals(), "the variable S2 is not defined" )
        
    def test_value(self) :
        myrad = np.loadtxt("bubbles.dat")
        n, mean = len(myrad), sum(myrad) / len(myrad)
        mys2 = ( n / (n-1) )*( sum(myrad*myrad/n) - mean*mean )
        self.assertTrue( np.abs( mys2 - S2 )<1e-7, "Your calculated variance in S2 is not correct" )
