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
                    time.sleep(0.01)  # Debounce delay for toggle

            if enabled:
                # Check if 'A' is pressed
                if not check_key_state('A'):  # 'A' is pressed
                    a_pressed = True
                elif a_pressed:  # 'A' was pressed and now is released
                    # Check if 'D' is manually pressed before executing automatic tap
                    if check_key_state('D'):  # 'D' not pressed by user
                        print("Key 'A' released. Tapping 'D'.")
                        tap_key('D')
                    a_pressed = False

                # Check if 'D' is pressed
                if not check_key_state('D'):  # 'D' is pressed
                    d_pressed = True
                elif d_pressed:  # 'D' was pressed and now is released
                    # Check if 'A' is manually pressed before executing automatic tap
                    if check_key_state('A'):  # 'A' not pressed by user
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
