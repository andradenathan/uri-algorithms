def lengthOfLongestSubstring(s: str) -> int:
  if s == "": return 0
  arr = []
  for i in s:
    if i not in arr:
      arr.append(i)

  return len(arr)

# it still getting the subsequence in this case but not the substring
print(lengthOfLongestSubstring("pwwkew"))