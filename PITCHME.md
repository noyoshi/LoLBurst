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

---?code=base.py&lang=python&title=Radix Tree

@[7-14](Here we are initializing the tree)
@[16-23](Here as well)

@[52-60](We simply add to a list for UnsortedList)
@[63-72](In sorted list, we sort the list after creating it)
@[72](Python provides an nlog n sort)
@[80-88](We stop searching after we stop finding elements in sorted list, as list is sortex lexographically)
@[97-99](The Trie begins with a root dictionary)
@[101-113](When inserting, we first check to see if an element is in this dict)
@[106-107](If it is, then we descend down the list)
@[108-110](Otherwise, we make a new entry in this level for it, and descend down it)
@[112](Once we have traversed the whole world, we set the end of word indicator)


