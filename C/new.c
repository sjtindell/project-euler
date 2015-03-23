#include <stdio.h>

int main(int argc, char *argv[])
{

	char head_string[] = {};
	sprintf(head_string, "euler%s.c", argv[1]);	

	FILE *fp = fopen(head_string, "a");
	fputs("#include <stdio.h>\n\n", fp);
	fputs("int main(int argc, char *argv[]);\n", fp);
	fputs("{\n\t", fp);
	fclose(fp);

	return 0;
}
