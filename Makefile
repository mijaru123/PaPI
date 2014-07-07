
UIPY = pyside-uic

SRC = ./ui/

DES = ./papi/ui/

UI_FILES = "$(shell find $(SRC) -regex ".*\.\(ui\)")"

comma:= ,
empty:=
space:= $(empty) $(empty)
foo:= a b c
bar:= $(subst $(space),$(comma),$(foo))

all:

	echo $$UI_FILES

#	$(foreach file,$(UI_FILES), echo $(file) )

	for UI_FILE in $(UI_FILES); do \
		echo "1" ; \
		F_NAME=$(basename $$UI_FILE ) ; \
		F_DIR=$(dir $$UI_FILE) ; \
		echo $$F_NAME ; \
		echo $$F_DIR ; \
	#	$(F_DIR) ; \
	done
