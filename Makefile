startup:
	-@mkdir data/ 2> /dev/null
	-@mkdir data/train/ 2> /dev/null
	-@mkdir data/lexed/ 2> /dev/null
	-@mkdir data/parsed/ 2> /dev/null
	@find data/raw/schematics -name "*.py" -print0 | xargs -0 -I file cp file ./data/train/

lex_all: startup
	@./scripts/lex_all

parse_all: startup
	@./scripts/parse_all

