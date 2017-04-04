import unittest

from bruch.Bruch import *


class TestAllgemein(unittest.TestCase):
    def setUp(self):
        self.b = Bruch(3, 2)
        self.b2 = Bruch(self.b)
        self.b3 = Bruch(4, 2)
        pass
    
    def tearDown(self):
        del self.b, self.b2, self.b3
        pass

    """
    Einen tuple (gleiche) Brüche erstellen und vergleichen
    """
    def testTuple(self):
        z, n = Bruch(3, 4)
        assert (z == 3 and n == 4)

    """
    Einen tuple (gleiche) Brüche erstellen, daraus einen Bruch erstellen und dann vergleichen
    """
    def testTuple2(self):
        z, n = self.b
        self.assertEqual(Bruch(z, n), self.b)

    """
    Brüche mit dem *= operator multiplizieren
    """
    def testMulti2(self):
        self.b *= Bruch(2)
        assert (self.b == 3)
        
    """
    Brüche mit dem *= operator multiplizieren
    """
    def testMulti2(self):
        self.b *= Bruch(2)
        assert (self.b == 3)
        
    """
    Brüche mit dem += operator addieren
    """
    def testiAdd2(self):
        self.b += Bruch(1)
        assert (self.b == Bruch(5, 2))

if __name__ == "__main__":
    unittest.main()
