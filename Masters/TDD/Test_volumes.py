import unittest
import volumes


class Test_volumes(unittest.TestCase):

    def test_get_cube_vol_basic1(self):
        self.assertEqual(volumes.get_cube_vol(3), 27)

    def test_get_cube_vol_basic2(self):
        self.assertEqual(volumes.get_cube_vol(4), 64)

<<<<<<< HEAD

=======
>>>>>>> 4c7d7a9c40cfa4d9bc260b91b049dfa2cad2942a
