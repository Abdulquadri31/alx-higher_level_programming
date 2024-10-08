#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about Python string objects
 * @p: PyObject string
 *
 * This function prints the type, length, and value of a Python string object.
 * If the object is not a valid string, an error message is printed.
 */
void print_python_string(PyObject *p)
{
    if (!PyUnicode_Check(p)) {
        printf("[ERROR] Invalid String Object\n");
        return;
    }

    // Determine whether it is ASCII or Unicode
    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";
    PyObject *str_repr = PyUnicode_AsUTF8String(p);
    const char *value = PyBytes_AsString(str_repr);

    // Print the string info
    printf("[.] string object info\n");
    printf("  type: %s\n", type);
    printf("  length: %ld\n", length);
    printf("  value: %s\n", value);

    // Decrement reference count for the temporary UTF-8 string
    Py_XDECREF(str_repr);
}
