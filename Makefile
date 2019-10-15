NAME = pbrain-gomoku-ai

all: ${NAME}

${NAME}:
	pyinstaller --onefile ${NAME}.py
	cp dist/${NAME} .

clean:
	rm -rf dist build ${NAME}.spec

fclean: clean
	rm -rf ${NAME}

re: fclean all