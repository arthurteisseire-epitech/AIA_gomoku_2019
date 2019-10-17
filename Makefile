NAME = pbrain-gomoku-ai

all: ${NAME}

${NAME}:
	cp ${NAME}.py ${NAME}
	chmod +x ${NAME}

fclean:
	rm -rf ${NAME}

re: fclean all
