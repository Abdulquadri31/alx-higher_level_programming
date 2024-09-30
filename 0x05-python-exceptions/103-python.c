#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
    
    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type_name = Py_TYPE(item)->tp_name;

        printf("Element %zd: %s\n", i, type_name);
        
        if (strcmp(type_name, "bytes") == 0) {
            print_python_bytes(item);
        } else if (strcmp(type_name, "float") == 0) {
            print_python_float(item);
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[.] bytes object info\n");
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *bytes_string = PyBytes_AsString(p);
    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", bytes_string);

    printf("  first %zd bytes: ", size > 10 ? 10 : size);
    for (Py_ssize_t i = 0; i < (size > 10 ? 10 : size); i++) {
        printf("%02x", (unsigned char)bytes_string[i]);
        if (i < (size > 10 ? 9 : size - 1)) {
            printf(" ");
        }
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[.] float object info\n");
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    double value = PyFloat_AsDouble(p);
    printf("[.] float object info\n");
    printf("  value: %f\n", value);
}
