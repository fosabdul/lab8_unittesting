
import unittest
from unittest import TestCase
from unittest.mock import patch


import lab8_Bitcoin 



class TestLab8_Bitcoin(TestCase):

    @patch('lab8_Bitcoin.request_bitcoin')
    def test_dollars_to_target_2(self, mock_rates):
        mock_rate = 10
        example_api_response = {"bpi":{"USD": {"code": "USD", "rate": mock_rate}}}
        mock_rates.side_effect = [ example_api_response ] 
        
        converted = lab8_Bitcoin.get_calculate(100, mock_rate)
        print(converted)
        expected = 1000
        self.assertEqual(expected, converted)

if __name__ == '__main__':
    unittest.main()

        
