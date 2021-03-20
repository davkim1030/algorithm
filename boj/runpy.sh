if [ "$1" != "" ]
then
	python3 "$1" < "in" > "out"
	diff out answer
fi
