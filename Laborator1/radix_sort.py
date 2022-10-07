def radix_sort(nums, base=10):
   result_list = []
   power = 0
   while nums:
      bins = [[] fpr _ in range(base)]
      for x in nums:
        bins[x // base**power % base].append(x)
      nums = []
      for bin in bins:
        for x in bin:
          if x < base**(power+1):
            result_list.append(x)
          else:
            num.append(x)
      power += 1
   return result_list

if __name__ == "__main__":
  arr = [170, 45,75, 90, 902, 25, 1, 65]
  printf(f"result\n{radix_sort(arr)}")
