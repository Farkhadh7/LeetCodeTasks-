EXPLANATION: Longest Common Prefix (LeetCode 14)

WHAT THE PROBLEM WANTS
You get a list of words, and you need to find the beginning part that every
word shares. For ["flower", "flow", "flight"], they all start with "fl", so
that's the answer. If they have nothing in common at the start, return "".


Take the first word and pretend the whole thing is the common prefix. It's
probably too long, but that's fine. Then go through the other words one by
one. Whenever a word doesn't start with our current guess, chop one letter
off the end of the guess and check again. Keep chopping until the word
matches. Once we've been through every word, whatever is left is the answer.

Think of it like trimming a piece of wood: you start long and shaveit down
until it fits every word.

WHAT EACH PART OF THE CODE DOES
- prefix = strs[0]
  Start with the first word as our guess. The answer can never be longer than
  this word, so it's a safe starting point.

- for s in strs[1:]
  Look at every other word, one at a time.

- while not s.startswith(prefix)
  Ask: "Does this word begin with my guess?" If not, the guess is too long.

- prefix = prefix[:-1]
  Cut the last letter off the guess and ask again.

- if prefix == "": return ""
  If we've cut it down to nothing, no prefix is shared, so we stop right away
  instead of wasting time. This also covers the case where one of the words
  is empty.

- return prefix
  If we make it through every word, the guess now fits all of them.

LET'S WALK THROUGH IT: ["flower", "flow", "flight"]
  Guess: "flower"
  Word "flow":    doesn't start with "flower" -> "flowe"
                  doesn't start with "flowe"  -> "flow"
                  starts with "flow", good.
  Word "flight":  doesn't start with "flow" -> "flo"
                  doesn't start with "flo"  -> "fl"
                  starts with "fl", good.
  Answer: "fl"

WHEN THERE'S NOTHING IN COMMON: ["dog", "racecar", "car"]
  Guess: "dog"
  Word "racecar": doesn't start with "dog" -> "do" -> "d" -> ""
  The guess is empty, so we return "" right away.

A COUPLE OF EDGE CASES
- One word only, like ["a"]: there's nobody to compare against, so the
  word itself is the answer.
- An empty word in the list, like ["", "abc"]: the guess starts as "", and
  every word "starts with" an empty string, so we correctly return "".

HOW FAST IS IT?
- Time: O(S), where S is the total number of letters across all the words.
  In the worst case we look at each letter about once.
- Space: O(1). We only keep one string (the guess), and it never gets
  longer than 200 characters.

NOTE
No type hints are used, so this works on both Python and Python3 in LeetCode.