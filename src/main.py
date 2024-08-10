import time
from strafe_tapper import check_key_state, tap_key

def main():
    print("Listening for 'A' and 'D' key releases. Press 'N' to toggle functionality. Press Ctrl+C to quit.")

    a_pressed = False
    d_pressed = False
    enabled = True  # Start with functionality enabled

    while True:
        try:
            # Check for toggle functionality with 'N'
            if not check_key_state('N'):  # 'N' is pressed
                enabled = not enabled
                print("Functionality enabled." if enabled else "Functionality disabled.")
                while not check_key_state('N'):  # Wait until 'N' is released
                    time.sleep(0.05)  # Debounce delay for toggle

            if enabled:
                # Check if 'A' is pressed
                if not check_key_state('A'):  # 'A' is pressed
                    if not a_pressed:
                        print("Key 'A' pressed.")
                    a_pressed = True
                elif a_pressed:  # 'A' was pressed and now is released
                    a_pressed = False
                    print("Key 'A' released.")
                    # Execute automatic tap if 'D' is not manually pressed
                    if check_key_state('D'):  # 'D' not pressed by user
                        print("Automatically tapping 'D'.")
                        tap_key('D')

                # Check if 'D' is pressed
                if not check_key_state('D'):  # 'D' is pressed
                    if not d_pressed:
                        print("Key 'D' pressed.")
                    d_pressed = True
                elif d_pressed:  # 'D' was pressed and now is released
                    d_pressed = False
                    print("Key 'D' released.")
                    # Execute automatic tap if 'A' is not manually pressed
                    if check_key_state('A'):  # 'A' not pressed by user
                        print("Automatically tapping 'A'.")
                        tap_key('A')

            # Small sleep to prevent excessive CPU usage
            time.sleep(0.005)  # Short sleep for better responsiveness

        except KeyboardInterrupt:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
