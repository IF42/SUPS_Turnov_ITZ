TEX=pdfcsplain
SRC=src
TARGET=UvodDoProgramovani
OUTPUT=pdf


all: env
		$(TEX) --output-directory=$(OUTPUT) $(SRC)/$(TARGET).tex


clean:
		rm -rvf $(OUTPUT)


env:
		mkdir -pv $(OUTPUT)
