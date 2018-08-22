}

int main(int argc, char* argv[])
{
	int x1, x2, x3, y;
	x1=atoi(argv[1]);
	y=pattern(x1);
	cout<<y;
	x2=atoi(argv[2]);
	y=pattern(x2);
	cout<<y;
	x3=atoi(argv[3]);
	y=pattern(x3);
	cout<<y;
	return 0;
}
