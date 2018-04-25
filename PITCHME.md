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

---?code=base.py&lang=python File

@title[Radix Tree in Python]

<p><span class="slide-title">Radix Tree (Trie)</span></p>

```
class Trie():
    def __init__(self):
        self.root = {}

    def insert(self, data):
        start = time.time()
        for elm in data:
            currlist = self.root
            for char in elm:
                if char.lower() in currlist.keys():
                    currlist = currlist[char.lower()]
                else:
                    currlist[char.lower()] = {}
                    currlist = currlist[char.lower()]

            currlist[0] = elm
        end = time.time()
        print("Insert: ",end-start)

    def search(self,data):
        start = time.time()
        currlist = self.root
        for char in data:
            if char in currlist.keys():
                currlist = currlist[char]
            else:
                end = time.time()
                print("Search: ", end-start)
                return []
        x = self.print_dictionary(currlist)
        end = time.time()
        print("Search: ", end-start)
        return x

    def print_dictionary(self, currlist):
        x = []

        if 0 in currlist.keys():
            x.append(currlist[0])


        for key in currlist.keys():
            if key != 0:
                x += self.print_dictionary(currlist[key])

        return x

```

@[1,2](You can present code inlined within your slide markdown too.)
@[9-17](Displayed using code-syntax highlighting just like your IDE.)
@[19-20](Again, all of this without ever leaving your slideshow.)

---?gist=onetapbeyond/494e0fecaf0d6a2aa2acadfb8eb9d6e8&lang=scala&title=Scala GIST

@[23](You can even present code found within any GitHub GIST.)
@[41-53](GIST source code is beautifully rendered on any slide.)
@[57-62](And code-presenting works seamlessly for GIST too, both online and offline.)

---

## Template Help

- [Code Presenting](https://github.com/gitpitch/gitpitch/wiki/Code-Presenting)
  + [Repo Source](https://github.com/gitpitch/gitpitch/wiki/Code-Delimiter-Slides), [Static Blocks](https://github.com/gitpitch/gitpitch/wiki/Code-Slides), [GIST](https://github.com/gitpitch/gitpitch/wiki/GIST-Slides) 
- [Custom CSS Styling](https://github.com/gitpitch/gitpitch/wiki/Slideshow-Custom-CSS)
- [Slideshow Background Image](https://github.com/gitpitch/gitpitch/wiki/Background-Setting)
- [Slide-specific Background Images](https://github.com/gitpitch/gitpitch/wiki/Image-Slides#background)
- [Custom Logo](https://github.com/gitpitch/gitpitch/wiki/Logo-Setting) [TOC](https://github.com/gitpitch/gitpitch/wiki/Table-of-Contents) [Footnotes](https://github.com/gitpitch/gitpitch/wiki/Footnote-Setting)

---

## Go GitPitch Pro!

<br>
<div class="left">
    <i class="fa fa-user-secret fa-5x" aria-hidden="true"> </i><br>
    <a href="https://gitpitch.com/pro-features" class="pro-link">
    More details here.</a>
</div>
<div class="right">
    <ul>
        <li>Private Repos</li>
        <li>Private URLs</li>
        <li>Password-Protection</li>
        <li>Image Opacity</li>
        <li>SVG Image Support</li>
    </ul>
</div>

---

### Questions?

<br>

@fa[twitter gp-contact](@gitpitch)

@fa[github gp-contact](gitpitch)

@fa[medium gp-contact](@gitpitch)

---?image=assets/image/gitpitch-audience.jpg&opacity=100

@title[Download this Template!]

### Get your presentation started!
### [Download this template @fa[external-link gp-download]](https://gitpitch.com/template/download/black)

