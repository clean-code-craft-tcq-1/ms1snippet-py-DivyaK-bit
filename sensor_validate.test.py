import unittest
import sensor_validate

class SensorValidatorTest(unittest.TestCase):
  def test_reports_error_when_soc_jumps(self):
    sensor_validate.If_Empty([0.0, 0.01, 0.5, 0.51], 0.05)
    sensor_validate.If_Empty([], 0.05)
  
  def test_reports_error_when_current_jumps(self):
    sensor_validate.If_Empty([0.03, 0.03, 0.03, 0.33], 0.1) 
    sensor_validate.If_Empty([], 0.1)

if __name__ == "__main__":
  unittest.main()
