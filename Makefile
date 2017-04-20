JPEG_ORIGINAL = $(shell find content/ -type f -name '*.jpg' ! -name '*__thumbnail-*' )
JPEG_SQUARE = $(patsubst %.jpg, %__thumbnail-square.jpg, $(JPEG_ORIGINAL))
JPEG_WIDE = $(patsubst %.jpg, %__thumbnail-wide.jpg, $(JPEG_ORIGINAL))

%__thumbnail-square.jpg: %.jpg
	convert  -geometry 800x800^ -gravity center -crop 800x800+0+0 "$<" "$@"

%__thumbnail-wide.jpg: %.jpg
	convert "$<" -resize "750>" "$@"

jpeg: $(JPEG_SQUARE) $(JPEG_WIDE)

clean:
	rm -rf ${JPEG_SQUARE}
	find . -name '*thumbnail*' -delete

run:
	hugo server --buildDrafts -w
