def array_insert_shift(list, obj)
  new_list = []
  mid_index = len(list) // 2

  for i in range(len(list)):
    if i < mid_index:
      new_list.append(list[i])
    elif i == mid_index:
      new_list.append(obj)
      new_list.append(list[i])
    else:
      new_list.append(list[i])
return(array_insert_shift(list, obj))
  