# Simple Blue Sky program (no pygame required)
import time
import os

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_blue_sky():
    """Display a simple blue sky representation in the console."""
    print("🌤️  Blue Sky Program 🌤️")
    print("=" * 30)
    
    # Create a simple sky representation
    sky_lines = [
        "    ☁️  ☁️  ☁️  ☁️  ☁️",
        "  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
        "☁️  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
        "    ☁️  ☁️  ☁️  ☁️  ☁️",
        "  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
        "☁️  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
        "    ☁️  ☁️  ☁️  ☁️  ☁️",
        "  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
        "☁️  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
        "    ☁️  ☁️  ☁️  ☁️  ☁️",
        "  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
        "☁️  ☁️  ☁️  ☁️  ☁️  ☁️  ☁️",
    ]
    
    # Display the sky with blue background effect
    for i, line in enumerate(sky_lines):
        # Add some color variation to simulate sky depth
        if i < 4:
            print(f"\033[94m{line}\033[0m")  # Darker blue
        elif i < 8:
            print(f"\033[96m{line}\033[0m")  # Medium blue
        else:
            print(f"\033[97m{line}\033[0m")  # Lighter blue
        time.sleep(0.1)  # Small delay for animation effect
    
    print("\n" + "=" * 30)
    print("✨ Beautiful blue sky! ✨")
    print("Press Enter to exit...")
    input()

if __name__ == "__main__":
    show_blue_sky()
