#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints Python strings
 * @p:  PyObject
 *
 * Return: void
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (PyUnicode_Check(p))
	{
		const char *type = PyUnicode_IS_COMPACT_ASCII(p)			? "compact ascii"
			: "compact unicode object";

		/* Get string length */
		Py_ssize_t length = PyUnicode_GET_LENGTH(p);

		/* Get string value */
		const char *value = PyUnicode_AsUTF8(p);

		/* Print string information */
		printf(" type: %s\n", type);
		printf(" length: %zd\n", length);
		prinft(" value: %s\n" value);
	} else
	{
		printf(" [ERROR] Invalid String Object\n");
	}
}
