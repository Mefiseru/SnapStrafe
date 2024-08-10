#include <Python.h>

#ifdef _WIN32
#include <windows.h>

// Function to check if a key is currently pressed
static PyObject* check_key_state(PyObject* self, PyObject* args) {
    char* key;
    if (!PyArg_ParseTuple(args, "s", &key))
        return NULL;

    SHORT keyState;
    if (strcmp(key, "A") == 0) {
        keyState = GetAsyncKeyState(0x41); // Virtual key code for 'A'
    } else if (strcmp(key, "D") == 0) {
        keyState = GetAsyncKeyState(0x44); // Virtual key code for 'D'
    } else if (strcmp(key, "N") == 0) {
        keyState = GetAsyncKeyState(0x4E); // Virtual key code for 'N'
    } else {
        Py_RETURN_FALSE;
    }

    // Return True if the key is currently pressed
    if (keyState & 0x8000) {
        Py_RETURN_FALSE;  // Key is pressed
    } else {
        Py_RETURN_TRUE;  // Key is released
    }
}

// Function to simulate a key tap with a longer hold duration
static PyObject* tap_key(PyObject* self, PyObject* args) {
    char* key;
    if (!PyArg_ParseTuple(args, "s", &key))
        return NULL;

    INPUT input = {0};
    input.type = INPUT_KEYBOARD;

    if (strcmp(key, "A") == 0) {
        input.ki.wVk = 0x41; // Virtual key code for 'A'
    } else if (strcmp(key, "D") == 0) {
        input.ki.wVk = 0x44; // Virtual key code for 'D'
    } else {
        Py_RETURN_FALSE;
    }

    // Press the key
    SendInput(1, &input, sizeof(INPUT));
    Sleep(50);  // Hold the key for 50 milliseconds (can adjust as needed)
    // Release the key
    input.ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(1, &input, sizeof(INPUT));

    Py_RETURN_TRUE;
}

#elif __linux__
#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>
#include <unistd.h>  // For usleep

static Display* display;
static Window root;

// Function to check if a key is currently pressed
static PyObject* check_key_state(PyObject* self, PyObject* args) {
    char* key;
    if (!PyArg_ParseTuple(args, "s", &key))
        return NULL;

    char keys_return[32];
    XQueryKeymap(display, keys_return);

    KeyCode keycode;
    if (strcmp(key, "A") == 0) {
        keycode = XKeysymToKeycode(display, XK_A);
    } else if (strcmp(key, "D") == 0) {
        keycode = XKeysymToKeycode(display, XK_D);
    } else if (strcmp(key, "N") == 0) {
        keycode = XKeysymToKeycode(display, XK_N);
    } else {
        Py_RETURN_FALSE;
    }

    // Return True if the key is currently pressed
    if (keys_return[keycode / 8] & (1 << (keycode % 8))) {
        Py_RETURN_FALSE;  // Key is pressed
    } else {
        Py_RETURN_TRUE;  // Key is released
    }
}

// Function to simulate a key tap with a longer hold duration
static PyObject* tap_key(PyObject* self, PyObject* args) {
    char* key;
    if (!PyArg_ParseTuple(args, "s", &key))
        return NULL;

    KeySym keysym;
    if (strcmp(key, "A") == 0) {
        keysym = XK_A;
    } else if (strcmp(key, "D") == 0) {
        keysym = XK_D;
    } else {
        Py_RETURN_FALSE;
    }

    KeyCode keycode = XKeysymToKeycode(display, keysym);
    XTestFakeKeyEvent(display, keycode, True, CurrentTime);
    usleep(50000);  // Hold the key for 50 milliseconds (can adjust as needed)
    XTestFakeKeyEvent(display, keycode, False, CurrentTime);
    XFlush(display);

    Py_RETURN_TRUE;
}

#endif

static PyMethodDef StrafeTapperMethods[] = {
    {"check_key_state", check_key_state, METH_VARARGS, "Check if a key is currently pressed."},
    {"tap_key", tap_key, METH_VARARGS, "Tap a key quickly with a hold."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef strafetappermodule = {
    PyModuleDef_HEAD_INIT,
    "strafe_tapper",
    NULL,
    -1,
    StrafeTapperMethods
};

PyMODINIT_FUNC PyInit_strafe_tapper(void) {
    #ifdef __linux__
    display = XOpenDisplay(NULL);
    if (display == NULL) {
        PyErr_SetString(PyExc_RuntimeError, "Unable to open X display");
        return NULL;
    }
    root = DefaultRootWindow(display);
    #endif

    return PyModule_Create(&strafetappermodule);
}
