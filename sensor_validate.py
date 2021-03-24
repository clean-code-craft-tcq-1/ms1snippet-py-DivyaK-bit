
def  Check_Range(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_charging_parameter_reading(values, delta_value):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not Check_Range(values[i], values[i + 1], delta_value)):
      return False
  return True

def If_Empty(value_list, delta_value):
  if not value_list:
    return validate_charging_parameter_reading(value_list, delta_value)
  else:
    print("List is empty")
    return False
