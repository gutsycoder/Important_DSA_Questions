#Pattern Matcher
# You're given two non-empty strings. The first one is a pattern consisting of only "x" s and/ or "y" s;
# the other one is a normal string of alphanumeric characters.
# Write a function that checks whether the normal string matches the pattern.
# A string So is said to match a pattern if replacing all "x" s in the pattern with some non-empty substring s1 of so and
# replacing all "y" s in the pattern with some non-empty substring S2 of so yields the same string so.
# If the input string doesn't match the input pattern, the function should return an empty array; otherwise,
# it should return an array holding the strings $1 and S2 that represent "x" and "y" in the normal string, in that order.
# If the pattern doesn't contain any "x" s or "y" s, the
# respective letter should be represented by an empty string in the final array that you return.
# You can assume that there will never be more than one pair of strings $1 and S2 that appropriately represent "x" and "y" in the
# normal string.
