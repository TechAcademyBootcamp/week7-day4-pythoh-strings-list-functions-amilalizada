def divide_string(str):
  if len(str) < 2:
    return 'cant'

  return str[0:2] + str[-2:]

print(divide_string('salam'))
