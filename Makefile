startup:
	-@mkdir data/ 2> /dev/null
	-@mkdir data/train/ 2> /dev/null
	-@mkdir data/lexed/ 2> /dev/null
	-@mkdir data/parsed/ 2> /dev/null
	-@mkdir data/ast/ 2> /dev/null
	@find data/raw/schematics -name "*.py" -print0 | xargs -0 -I file cp file ./data/train/

lex_training: startup
	@./scripts/lex_training

parse_training: startup
	@./scripts/parse_training

training_asts: startup
	@./scripts/training_asts

ast_explore: startup
	@python src/ast_magic.py
