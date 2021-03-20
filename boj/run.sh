if [ "$1" != "" ]
then
	g++ "$1" -o exec
	./exec < "in" > out
	diff out answer
	rm exec
fi
