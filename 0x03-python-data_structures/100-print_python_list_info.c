#include <Python.h>

/**
 * print_python_list_info - prints basic info about a Python list
 * @p: pointer to the Python object (should be a list)
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list_obj = (PyListObject *)p;
    Py_ssize_t size, allocated, i;
    PyObject *element;

    if (PyList_Check(p))
    {
        size = PyList_Size(p); /* Get the number of elements in the list */
        allocated = list_obj->allocated; /* Get the allocated space for the list */

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", allocated);

        for (i = 0; i < size; i++)
        {
            element = PyList_GetItem(p, i); /* Get the item at index i */
            printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name); /* Print the type of the element */
        }
    }
    else
    {
        fprintf(stderr, "Provided object is not a list\n");
    }
}
