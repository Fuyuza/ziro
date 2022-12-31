# ziro
Hide message in message using zero width character

# Setup
```py
pip install git+https://github.com/Fuyuza/ziro/
```

# Usage
```py
ziro.hide("Your Message", "Your Hidden Message")
```
> -> will return "Your Message" with hidden message

```py
ziro.reveal("Your Message")
```
> -> will return "Hidden Message"

