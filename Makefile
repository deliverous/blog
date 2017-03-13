JPEG_ORIGINAL = $(shell find content/ -type f -name '*.jpg' ! -name '*__thumbnail-*' )
JPEG_SQUARE = $(patsubst %.jpg, %__thumbnail-square.jpg, $(JPEG_ORIGINAL))

%__thumbnail-square.jpg: %.jpg
	convert "$<" -resize "800>" -quality 70 "$@"

jpeg: $(JPEG_SQUARE)
