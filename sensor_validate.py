
def  Check_Range(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_charging_parameter_reading(values, delta_value):
  if len(values) == 0:
    print("There are no Values present to Validate, Please provide some")
    return False
  else:
    last_but_one_reading = len(values) - 1
    for i in range(last_but_one_reading):
      if(not Check_Range(values[i], values[i + 1], delta_value)):
        return False
  return True
