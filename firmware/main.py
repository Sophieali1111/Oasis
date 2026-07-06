import time
import sys
from pymavlink import mavutil

UART_DEVICE = "/dev/ttyAMA0"
BAUDRATE = 115200
MOTOR_COUNT = 4
TEST_THROTTLE = 5  # 5% Throttle
HOLD_DELAY = 2.0    # 2 seconds duration per test


def connect_fc():
    print(f"Connecting to {UART_DEVICE} at {BAUDRATE} baud...")
    mav = mavutil.mavlink_connection(UART_DEVICE, baud=BAUDRATE)
    print("Waiting for heartbeat...")
    mav.wait_heartbeat(timeout=10)
    print(f"Connected: system {mav.target_system}, component {mav.target_component}")
    return mav


def run_motor_test(mav, motor_num, throttle_percent, duration_secs):
    """
    Executes ArduPilot's native MAV_CMD_DO_MOTOR_TEST command.
    """
    # Param 1: Motor sequence number (1-indexed)
    # Param 2: Throttle type (0 = Throttle percentage 0-100)
    # Param 3: Throttle value
    # Param 4: Timeout in seconds
    # Param 5: Motor count (1 for an individual motor)
    # Param 6: Motor test types (0 for default/standard frame order)
    
    mav.mav.command_long_send(
        mav.target_system, 
        mav.target_component,
        mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST, 
        0,                 # Confirmation
        motor_num,         # Param 1
        0,                 # Param 2 (0 means percent-based)
        throttle_percent,  # Param 3
        duration_secs,     # Param 4
        1,                 # Param 5
        0, 0               # Param 6, 7
    )
    
    # Check for acknowledgement response from Flight Controller
    ack = mav.recv_match(type="COMMAND_ACK", blocking=True, timeout=2)
    if ack and ack.command == mavutil.mavlink.MAV_CMD_DO_MOTOR_TEST:
        if ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED:
            return True
    return False


def test_individual_motor(mav, motor_num):
    print(f"\n--- Motor {motor_num} ---")
    input(f"Press Enter to spin motor {motor_num} at {TEST_THROTTLE}% for {HOLD_DELAY}s...")
    
    if run_motor_test(mav, motor_num, TEST_THROTTLE, HOLD_DELAY):
        print(f"Motor {motor_num} spinning...")
        time.sleep(HOLD_DELAY + 0.5)  # Let it finish spinning completely
        print(f"Motor {motor_num} finished cycle.")
    else:
        print(f"Flight Controller rejected command for Motor {motor_num}. Ensure safety switch is pressed/disabled.")


def main():
    mav = None
    try:
        mav = connect_fc()

        # REMOVED manual arming sequence. 
        # ArduPilot's motor test command manages its own overriding spin-state safely.

        for i in range(1, MOTOR_COUNT + 1):
            test_individual_motor(mav, i)

        print("\n=== All individual tests complete ===")

    except KeyboardInterrupt:
        print("\nInterrupted.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if mav:
            mav.close()
        print("Done.")


if __name__ == "__main__":
    main()