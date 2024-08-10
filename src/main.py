import time
from strafe_tapper import check_key_release, tap_key

def main():
    print("Listening for 'A' and 'D' key releases. Press Ctrl+C to quit.")

    a_pressed = False
    d_pressed = False

    while True:
        try:
            # Check if 'A' is pressed
            if not check_key_release('A'):  # 'A' is pressed
                a_pressed = True
            elif a_pressed:  # 'A' was pressed and now is released
                print("Key 'A' released. Tapping 'D'.")
                tap_key('D')
                a_pressed = False

            # Check if 'D' is pressed
            if not check_key_release('D'):  # 'D' is pressed
                d_pressed = True
            elif d_pressed:  # 'D' was pressed and now is released
                print("Key 'D' released. Tapping 'A'.")
                tap_key('A')
                d_pressed = False

            # Small sleep to prevent excessive CPU usage
            time.sleep(0.01)

        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
