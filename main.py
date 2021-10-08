def merger(lists):
  mergedList = []

  for listinlist in lists:
    for i in listinlist:
      mergedList.append(i)

  mergedList.sort()

  return mergedList

