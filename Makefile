JPEG_ORIGINAL = $(shell find content/ -type f -name '*.jpg')
JPEG_SQUARE = $(patsubst content/%.jpg, public/%__square.jpg, $(JPEG_ORIGINAL))

public/%__square.jpg: content/%.jpg
	convert "$<" -resize "800>" -quality 70 "$@"

jpeg: $(JPEG_SQUARE)
