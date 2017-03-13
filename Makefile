JPEG_ORIGINAL = $(shell find content/ -type f -name '*.jpg' ! -name '*__thumbnail-*' )
JPEG_SQUARE = $(patsubst %.jpg, %__thumbnail-square.jpg, $(JPEG_ORIGINAL))

%__thumbnail-square.jpg: %.jpg
	convert  -geometry 360x360^ -gravity center -crop 360x360+0+0 "$<" "$@"

jpeg: $(JPEG_SQUARE)

clean:
	rm -rf ${JPEG_SQUARE}
	find . -name '*thumbnail*' -delete

run:
	hugo server --buildDrafts -w
