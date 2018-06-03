#!/usr/bin/python

def nested(depth,val):
  if depth <= 1:
    return [val]
  else:
    return [nested(depth -1, val)]

def nested_list(num):
  list = []
  for i in range(num):
    if i == 0:
      list.append(num)
    else:
      list.append(nested(i, i))
  return list

def flatten(list):
  results = []
  for item in list:
    if type(item) == type([]):
      results.extend(flatten(item))
    else
      results.append(item)
  return results
