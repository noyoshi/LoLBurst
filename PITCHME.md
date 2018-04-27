# LoL Burst 

### Tim Blazek, Edward Atkinson, Noah Yoshida

---

## What is it?

<br>

@fa[database gp-tip](Game data info)

@fa[github gp-tip](Open source platform)

---

## Our use of data structures

<br>

Besides the obvious... We used a *Radix Tree* to help autocomplete search
parameters

---?code=base.py&lang=python&title=Code Walkthrough

@[52-60](We simply add to a list for UnsortedList)
@[63-72](In sorted list, we sort the list after creating it)
@[72](Python provides an nlog n sort)
@[75-88](Search is optimized for sorted list as well)
@[80-88](We stop searching after we stop finding elements in sorted list, as list is sortex lexographically)
@[97-99](The Trie begins with a root dictionary)
@[101-113](When inserting, we first check to see if an element is in this dict)
@[106-107](If it is, then we descend down the list)
@[108-110](Otherwise, we make a new entry in this level for it, and descend down it)
@[112](Once we have traversed the whole word, we set the end of word indicator)
@[116-129](Searching)
@[116-118](When we search, we begin with the root)
@[119-121](We traverse the word, and see if the character is in the current level)
@[122-125](If we do not find the end of the word, then we return nothing)
@[126-129](Otherwise, we know the word is in the tree, and get the word)
@[131-138](When we print_dictionary, we recursavely traverse until we find the end of word key, and copy that to x)
